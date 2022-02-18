from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ranking = models.FloatField(max_length=20, null=True)
    image = models.ImageField(upload_to='bluckbuster/media')

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='bluckbuster/media/categories', blank=True)

    class Meta:
        db_table = 'Category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(max_length=100, unique=True, blank=True, null=False)
    description = models.TextField()
    images = models.ImageField(upload_to='bluckbuster/media/products', blank=True, null=False, default=False)
    is_image = models.BooleanField(default=False)
    ranking = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    categories = Category.category_name
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    class Meta:
        db_table = 'Product'
