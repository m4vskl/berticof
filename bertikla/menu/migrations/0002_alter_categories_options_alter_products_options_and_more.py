# Generated by Django 4.2.11 on 2024-04-12 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Ürün', 'verbose_name_plural': 'Ürünler'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='description',
            field=models.TextField(max_length=100, verbose_name='Kategori Açıklaması'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Kategori İsmi'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='order',
            field=models.IntegerField(default=0, null=True, verbose_name='Sıra'),
        ),
        migrations.AlterField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Stok Durumu'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.categories', verbose_name='Bağlı Olduğu Kategori'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(max_length=100, verbose_name='Ürün Açıklaması'),
        ),
        migrations.AlterField(
            model_name='products',
            name='ingredients',
            field=models.TextField(max_length=100, verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Aktif Mi?'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Ürün İsmi'),
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(upload_to='products/', verbose_name='Ürün Fotoğrafı'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ürün Fiyatı'),
        ),
    ]
