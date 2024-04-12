from django.db import models


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Kategori İsmi')
    description = models.TextField(max_length=100, verbose_name='Kategori Açıklaması')
    order = models.IntegerField(null=True, default=0, verbose_name='Sıra')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
    def __str__(self):
        return self.name


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Ürün İsmi')
    description = models.TextField(max_length=100, verbose_name='Ürün Açıklaması')
    photo = models.ImageField(upload_to='products/', null=False, blank=False, verbose_name='Ürün Fotoğrafı')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ürün Fiyatı')
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Bağlı Olduğu Kategori')
    ingredients = models.TextField(max_length=100, verbose_name='İçerik')
    available = models.BooleanField(default=True, verbose_name='Stok Durumu')
    is_active = models.BooleanField(default=True, verbose_name='Aktif Mi?')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'
    def __str__(self):
        return self.name
