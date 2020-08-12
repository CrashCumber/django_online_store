from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    definition = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.title


class Banner(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    definition = models.CharField(max_length=100)

    def __str__(self):
        return self.title
