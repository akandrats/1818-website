from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    '''
    INSERT INTO table_name (name, description, price, image )
    VALUES ("T-shirt", "My desc", 10, ...); 
    '''

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'catalog'

