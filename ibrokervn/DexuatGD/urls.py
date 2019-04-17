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
    #url("^feeds/(?P<format>.*)%s$" % _slash, views.Nhandinh_feed, name="Nhandinh_feed"),
    #url("^tag/(?P<tag>.*)/feeds/(?P<format>.*)%s$" % _slash, views.Nhandinh_feed, name="Nhandinh_feed_tag"),
    url(r'^import_Doanhnghiep/', views.import_Stock_basic_info , name='import'),
    url("^tag/(?P<tag>.*)%s$" % _slash,
        views.Nhandinh_list, name="NhandinhTT_DexuatGD_list_tag"),
    #url("^category/(?P<category>.*)/feeds/(?P<format>.*)%s$" % _slash,views.Nhandinh_feed, name="Nhandinh_feed_category"),
    url("^category/(?P<category>.*)%s$" % _slash,
        views.Nhandinh_list, name="NhandinhTT_DexuatGD_list_category"),
    #url("^author/(?P<username>.*)/feeds/(?P<format>.*)%s$" % _slash, views.Nhandinh_feed, name="Nhandinh_feed_author"),
    url("^author/(?P<username>.*)%s$" % _slash,
        views.Nhandinh_list, name="NhandinhTT_DexuatGD_list_author"),
    url("^archive/(?P<year>\d{4})/(?P<month>\d{1,2})%s$" % _slash,
        views.Nhandinh_list, name="NhandinhTT_DexuatGD_list_month"),
    url("^archive/(?P<year>\d{4})%s$" % _slash,
        views.Nhandinh_list, name="NhandinhTT_DexuatGD_list_year"),
    url("^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/"
        "(?P<slug>.*)%s$" % _slash,
        views.Nhandinh_detail, name="Nhandinh_detail_day"),
    url("^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>.*)%s$" % _slash,
        views.Nhandinh_detail, name="Nhandinh_detail_month"),
    url("^(?P<year>\d{4})/(?P<slug>.*)%s$" % _slash,
        views.Nhandinh_detail, name="Nhandinh_detail_year"),
    url("^nhandinhmoinhat%s$" % _slash, views.Nhandinh_detail_moinhat, name='newest'),
    url("^(?P<slug>.*)%s$" % _slash, views.Nhandinh_detail, name='daily'),

    url("^$", views.Nhandinh_list, name="NhandinhTT_DexuatGD_list"),

    #url("^$", views.Nhandinh_detail_moinhat, name="nhandinh_detail_moinhat"),
      ]