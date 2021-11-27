from django.core.management.base import BaseCommand
import json, os
from mainapp.models import ProductsCategory, Product
from authapp.models import ShopUser

JSON_PATH = 'mainapp/jsons/'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='utf8') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        catigories = load_from_json('categories')
        ProductsCategory.objects.all().delete()
        for category in catigories:
            new_category = ProductsCategory(**category)
            new_category.save()
        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductsCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()
        super_user = ShopUser.objects.create_superuser('admin', 'admin@geekshop.local', 'qwe', age=30)
        if super_user:
            print('Super user create...')
