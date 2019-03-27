from __future__ import unicode_literals
from future.builtins import str, int

from calendar import month_name

from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _


from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import paginate

User = get_user_model()

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
import django_excel as excel
from .models import Stock_Detail, Recommend, Recommend_Category
from django.contrib.admin.views.decorators import staff_member_required

# Create data Stock's basic info from excel.

data =[1, 2, 3]
class UploadFileForm(forms.Form):
    file = forms.FileField()

@staff_member_required
def import_Stock_basic_info(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=0,
                model=Stock_Detail,
                mapdict=[   'Symbol',
                            'Name',
                            'San',
                            'Website',
                            'So_dien_thoai',
                            'Dia_chi',
                            'Quan',
                            'Tinh',
                            'Tong_Quan',
                            'Industry',
                            'SL_CP_Niem_yet',
                            'Ty_le_Freeloat',
                            'Ty_le_SHNN',
                            ]
            )
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    template = "pages/toidautu/nhandinhthitruong/import_Doanhnghiep.html"
    context = {'form': form}

    return render(
        request,
        template,
        context)



def Nhandinh_detail_moinhat(request, tag=None, year=None, month=None, username=None,
                   category=None, template="pages/toidautu/NhandinhTT_DexuatGD.html",
                   extra_context=None):
    Nhandinh_posts = Recommend.objects.published(for_user=request.user)
    Post_moinhat_1 = Nhandinh_posts.latest('publish_date')
    Post_moinhat_60 = Nhandinh_posts.order_by('-publish_date')[:60]
    templates = []
    if tag is not None:
        tag = get_object_or_404(Keyword, slug=tag)
        Nhandinh_posts = Nhandinh_posts.filter(keywords__keyword=tag)
    if year is not None:
        Nhandinh_posts = Nhandinh_posts.filter(publish_date__year=year)
        if month is not None:
            Nhandinh_posts = Nhandinh_posts.filter(publish_date__month=month)
            try:
                month = _(month_name[int(month)])
            except IndexError:
                raise Http404()
    if category is not None:
        category = get_object_or_404(Recommend_Category, slug=category)
        Nhandinh_posts = Nhandinh_posts.filter(categories=category)
        templates.append(u"pages/toidautu/NhandinhTT_DexuatGD_%s.html" %
                          str(category.slug))
    author = None
    if username is not None:
        author = get_object_or_404(User, username=username)
        Nhandinh_posts = Nhandinh_posts.filter(user=author)
        templates.append(u"pages/toidautu/NhandinhTT_DexuatGD_%s.html" % username)

    prefetch = ("categories", "keywords__keyword")
    Nhandinh_posts = Nhandinh_posts.select_related("user").prefetch_related(*prefetch)
    Nhandinh_posts = paginate(Nhandinh_posts, request.GET.get("page", 1),
                          settings.BLOG_POST_PER_PAGE,
                          settings.MAX_PAGING_LINKS)

    context = {"Post_moinhat_60": Post_moinhat_60,"Post_moinhat_1": Post_moinhat_1, "year": year, "month": month,
               "tag": tag, "category": category, "author": author}
    context.update(extra_context or {})
    templates.append(template)
    return TemplateResponse(request, templates, context)



