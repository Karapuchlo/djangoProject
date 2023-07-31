from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from catalog.models import Product


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/main.html'
    my_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.my_context)
        return context


class CatalogPageView(TemplateView):
    template_name = 'catalog/catalog.html'
    extra_context = {'title': 'Каталог'}


class ContactsPageView(TemplateView):
    template_name = 'catalog/contact.html'
    extra_context = {'title': 'Контакты'}

class ProductPageView(TemplateView):
    model = Product
    template_name = 'catalog/product.html'
    my_context = {'title': 'Товар'}


def product(request, pk):
       product_item = Product.objects.get(pk=pk)
       context = {
           'object': product_item,
           'title': product_item.name
       }
       return render(request, 'catalog/product.html', context)