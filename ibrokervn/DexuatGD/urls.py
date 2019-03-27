from __future__ import unicode_literals

from mezzanine.conf import settings


# Trailing slahes for urlpatterns based on setup.
_slash = "/" if settings.APPEND_SLASH else ""


from django.conf.urls import url
from DexuatGD import views


app_name='DexuatGD'
urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # The home page
    url("^(?P<slug>.*)%s$" % _slash, views.Nhandinh_detail_moinhat, name='daily'),

    url(r'import_Doanhnghiep', views.import_Stock_basic_info , name='index'),
    url("^$", views.Nhandinh_detail_moinhat, name="nhandinh_detail_moinhat"),
      ]