from django.conf.urls import url
from Stock_detail import views


app_name='Stock_detail'
urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # The home page
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.Stock_Detail,
        name='Stock_detail_2'),
    url(r'import_Doanhnghiep$', views.import_Stock_basic_info , name='index'),
      ]