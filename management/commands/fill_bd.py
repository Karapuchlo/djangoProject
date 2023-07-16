import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data.json') as file:
            content = json.load(file)

        categories_create = []
        products_create = []

        for model in content:
            if model['model'] == 'catalog.category':
                categories_create.append(Category(pk=model['pk'],
                                                      category_name=model['fields']['category_name'],
                                                      category_description=model['fields']['category_description']))
            elif model['model'] == 'catalog.product':
                products_create.append(Product(name=model['fields']['name'],
                                                   description=model['fields']['description'],
                                                   img=model['fields']['img'],
                                                   price=model['fields']['price'],
                                                   category_id=model['fields']['category']))
            else:
                continue

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_create)

        Product.objects.all().delete()
        Product.objects.bulk_create(products_create)