from django.test import TestCase
from mainapp.models import Product, ProductsCategory


class ProductsTestCase(TestCase):
    def setUp(self):
        category = ProductsCategory.objects.create(name="������")
        self.product_1 = Product.objects.create(name="���� 1",
                                                category=category,
                                                price=1999.5,
                                                quantity=150)

        self.product_2 = Product.objects.create(name="���� 2",
                                                category=category,
                                                price=2998.1,
                                                quantity=125,
                                                is_active=False)

        self.product_3 = Product.objects.create(name="���� 3",
                                                category=category,
                                                price=998.1,
                                                quantity=115)

    def test_product_get(self):
        product_1 = Product.objects.get(name="���� 1")
        product_2 = Product.objects.get(name="���� 2")
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = Product.objects.get(name="���� 1")
        product_2 = Product.objects.get(name="���� 2")
        self.assertEqual(str(product_1), '���� 1 (������)')
        self.assertEqual(str(product_2), '���� 2 (������)')

    # def test_product_get_items(self):
    #     product_1 = Product.objects.get(name="���� 1")
    #     product_3 = Product.objects.get(name="���� 3")
    #     products = product_1.get_items()
    #
    #     self.assertEqual(list(products), [product_1, product_3])