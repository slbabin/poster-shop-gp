from django.db import models

class Category(models.Model):
        
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Poster(models.Model):
    sku = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)    
    title = models.CharField(max_length=255)
    description = models.TextField()
    artist = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    year = models.PositiveIntegerField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title