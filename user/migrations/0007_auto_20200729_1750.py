# Generated by Django 3.0.8 on 2020-07-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_component'),
        ('user', '0006_cartproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='likeProduct',
            field=models.ManyToManyField(related_name='like_product', through='user.LikeProduct', to='product.Product'),
        ),
    ]
