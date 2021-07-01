from django.db import models


class Products(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=256)
    pub_date = models.DateField()
