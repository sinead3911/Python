from django.conf.urls import url
from .views import gallery

urlpatterns = [
    url(r'^$', gallery, name='gallery'),
   
]