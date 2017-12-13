from django.conf.urls import url
from .views import flavours

urlpatterns = [
    url(r'^$', flavours, name='flavours'),
]