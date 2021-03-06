# Generated by Django 2.0.6 on 2018-07-16 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentid', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=13)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Category')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=40)),
                ('featureid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.FeatureLookup')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.SlugField(max_length=30)),
                ('type', models.CharField(max_length=10)),
                ('isactive', models.BooleanField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('brandid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Brand')),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactname', models.CharField(max_length=20)),
                ('businessname', models.CharField(max_length=20)),
                ('phone1', models.CharField(max_length=13)),
                ('phone2', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=40)),
                ('gstin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('datetime', models.DateTimeField()),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Order')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('hno', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('pin', models.IntegerField()),
                ('landmark', models.CharField(max_length=100)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.customer')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sellerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Seller'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='productid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='addressid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.ShippingAddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='customerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.customer'),
        ),
        migrations.AddField(
            model_name='featurevalue',
            name='productid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='customerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='productid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Product'),
        ),
    ]
