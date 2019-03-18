from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
import django_excel as excel
from .models import Stock_Detail
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
    template = "pages/toidautu/ThongtinDN/import_Doanhnghiep.html"
    context = {'form': form}

    return render(
        request,
        template,
        context)


"""
def Stock_detail(request):
    context = {}
    template = loader.get_template('phantichcophieu.html')
    return HttpResponse(template.render(context, request))

"""

# Create your views here.
