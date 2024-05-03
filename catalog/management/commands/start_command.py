import json
from django.core.management import BaseCommand
from catalog.models import Category, Product
from django.db import connection


class Command(BaseCommand):

    def handle(self, *args, **options):

        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;') # рестарт id

        Category.objects.all().delete()
        Product.objects.all().delete()

        with open('fixtures/data.json', encoding='utf-8') as json_file:
            data = json.load(json_file)

            product_for_create = []
            category_for_create = []

            for item in data:
                if item['model'] == 'catalog.category':
                    category_for_create.append(Category(name=item['fields']['name'],
                                                        description=item['fields'][
                                                            'description']))
            Category.objects.bulk_create(category_for_create)

            for item in data:
                if item['model'] == 'catalog.product':
                    product_for_create.append(Product(name=item['fields']['name'],
                                                      category=Category.objects.get(pk=item['fields']['category']),
                                                      price=item['fields']['price']))
            Product.objects.bulk_create(product_for_create)
