from django.conf.urls import url

from django.conf.urls.i18n import i18n_patterns
from GDNN import views

app_name='GDNN'
urlpatterns = i18n_patterns (
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.

    url(r'import_GDNN',views.import_GDNN, name='import_gdnn'),
    url(r'$',views.TKgdnn, name='gdnn'),
    # url(r'chienluocGD.html$', views.Trading_strategy, name='vimo1'),
)

