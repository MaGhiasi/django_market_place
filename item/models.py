from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # to order items in category based on their name
        ordering = ('name',)
        # to correct misspell in superuser models
        verbose_name_plural = 'Categories'

    def __str__(self):
        # to show name of each category instead of column
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    # longer than 5 char, if user doesn't want this field is OK
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    # it goes to folder item_images
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # to order items in category based on their name
        ordering = ('name',)
        # to correct misspell in superuser models
        verbose_name_plural = 'Items'

    def __str__(self):
        # to show name of each category instead of column
        return self.name