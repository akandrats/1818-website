import os
import django
from catalog.models import Product

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

django.setup()

new_product = Product.objects.create(
    name='T-shirt',
    description='My desc',
    price=10,
    image='/static/1856059808_1_1_1.jpg'
)

new_product.save()

