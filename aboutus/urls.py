from django.conf.urls import url
from .views import aboutus

urlpatterns = [
    url(r'^$', aboutus, name='aboutus'),
]