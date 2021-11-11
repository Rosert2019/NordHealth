from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):

    name = models.CharField('Name of the product', max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField('Upload an image', upload_to='products/', blank=True)
    description = models.TextField('Add a desciption of the dish', blank=True)
    price = models.DecimalField('Add a price. ',max_digits=10, decimal_places=2)
    code = models.CharField('Add a code', max_length = 20)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
  
    
    class Meta:
        ordering = ('name', 'price') #we need to have all product sorted by name and by code in the templates
         
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:productDetail', args=[self.id, self.slug])
