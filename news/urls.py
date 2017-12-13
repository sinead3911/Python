from django.conf.urls import url
from .views import news

urlpatterns = [
    url(r'^$', news, name='news'),
]