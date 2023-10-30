from django.db import models

class Category(models.Model):
    parent=models.ForeignKey('self',verbose_name='parant',blank=True,null=True ,on_delete= models.CASCADE)
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

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(verbose_name='title', max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='products/')
    is_enable = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category',verbose_name='categories',blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='pruducts'
        verbose_name='Product'
        verbose_name_plural='Products'

    def __str__(self):
        return self.title

class File(models.Model):
    product=models.ForeignKey('Product',related_name='files', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=50)
    file =models.FileField(upload_to='files/')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='files'
        verbose_name='File'
        verbose_name_plural='Files'

    def __str__(self):
        return self.title

