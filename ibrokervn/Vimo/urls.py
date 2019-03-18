from django.conf.urls import url
from Vimo import views
from django.conf.urls.i18n import i18n_patterns





app_name='Vimo'
urlpatterns = i18n_patterns (
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.


    url(r'^$',views.Vimo_list, name='vimo'),
    # url(r'chienluocGD.html$', views.Trading_strategy, name='vimo1'),
)


