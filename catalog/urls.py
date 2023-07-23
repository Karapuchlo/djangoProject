from django.contrib import admin
from django.urls import path

from catalog.views import index, contact, catalog, product

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', index),
    path('contact/', contact),
    path('catalog/', catalog),
   path('product', product)
]
