"""workflowapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from todoitem.views import get_index,add_item,edit_item,toggle_item
from accounts import urls as accounts_urls
from donations.views import all_products
from donations import urls as product_urls
from .settings import MEDIA_ROOT
from cart import urls as urls_cart

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name="home"),
    url(r'^donations/', include(product_urls)),
    url(r'add$', add_item,),
    url(r'^edit/(\d+)$', edit_item),
    url(r'^toggle/(\d+)$', toggle_item),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^cart/', include(urls_cart)),
]