"""cakes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import urls as blog_urls
from blog.views import blogposts
from products.views import all_products
from accounts import urls as accounts_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from products import urls as products_urls
from django.views import static
from .settings import MEDIA_ROOT
from gallery import urls as gallery_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name='home'),
    url(r'^products/', include(products_urls)),
    url(r'^$', blogposts, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^gallery/', include(gallery_urls)),
]
