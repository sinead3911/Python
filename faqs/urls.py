from django.conf.urls import url
from .views import faqs

urlpatterns = [
    url(r'^$', faqs, name='faqs'),
]