from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=200)
    product_price = models.CharField(max_length=200)
    product_quantity = models.CharField(max_length=200)
    product_img_url = models.CharField(max_length=200)
    bid_value = models.IntegerField()

    def __str__(self):
            return '%s %s' % (self.product_name, self.product_code)