from django.db import models

class Category(models.Model):
    title = models.CharField(verbose_name='title', max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to= 'categoris/')
    is_enable = models.BooleanField(default=True)
    created_time =models.DateTimeField(auto_now_add=True)
    updated_time =models.DateTimeField(auto_now=True)

    class Meta:
        db_table='categoris'
        verbose_name='Category'
        verbose_name_plural='Categories'

class Product(models.Model):
    title = models.CharField(verbose_name='title', max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='products/')
    is_enable = models.BooleanField(default=True)
    categories=models.ManyToManyField('Category',verbose_name='categories',blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='pruducts'
        verbose_name='Product'
        verbose_name_plural='Products'

class File(models.Model):
    product=models.ForeignKey('Product', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=50)
    File =models.FileField(upload_to='files/')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='files'
        verbose_name='File'
        verbose_name_plural='Files'

