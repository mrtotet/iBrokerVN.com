from django.conf.urls import url
from Main import views


app_name='Main'
urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # The home page
    url(r'chienluocgiaodich$', views.Trading_strategy , name='index'),
      ]