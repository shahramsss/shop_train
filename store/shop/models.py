from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    sub_categry = models.ForeignKey('self', on_delete=models.CASCADE , null= True , blank=True , related_name='scategory')
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_filter' , args=[self.slug,])


class Product(models.Model):
    category = models.ManyToManyField(
        Category, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='product/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:productdetail' , args=[self.slug,])