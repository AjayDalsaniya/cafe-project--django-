# Generated by Django 4.1.3 on 2023-02-07 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0075_table_total_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('idpurchase', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_total_amount', models.IntegerField()),
                ('purchase_date', models.DateField()),
                ('gst', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
            options={
                'db_table': 'purchase',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PurchaseReturn',
            fields=[
                ('idpurchase_return', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_return_total_amount', models.IntegerField()),
                ('purchase_return_date', models.DateField()),
                ('purchase_idpurchase', models.ForeignKey(db_column='purchase_idpurchase', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.purchase')),
            ],
            options={
                'db_table': 'purchase_return',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('idsupplier', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=60)),
                ('supplier_mobile_no', models.DecimalField(decimal_places=0, max_digits=10)),
                ('supplier_address', models.CharField(max_length=200)),
                ('area_name', models.CharField(max_length=200)),
                ('pincode', models.DecimalField(decimal_places=0, max_digits=6)),
                ('restaurant_idrestaurant', models.ForeignKey(db_column='restaurant_idrestaurant', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.restaurant')),
            ],
            options={
                'db_table': 'supplier',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('idraw_material', models.AutoField(primary_key=True, serialize=False)),
                ('raw_material_name', models.CharField(max_length=60)),
                ('raw_materialtotal_quantity', models.IntegerField()),
                ('raw_material_price', models.IntegerField()),
                ('restaurant_idrestaurant', models.ForeignKey(db_column='restaurant_idrestaurant', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.restaurant')),
            ],
            options={
                'db_table': 'raw_material',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PurchaseReturnOfRawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('purchase_return_idpurchase_return', models.ForeignKey(db_column='purchase_return_idpurchase_return', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.purchasereturn')),
                ('raw_material_idraw_material', models.ForeignKey(db_column='raw_material_idraw_material', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.rawmaterial')),
            ],
            options={
                'db_table': 'purchase_return_of_raw_material',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PurchaseRawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('purchase_idpurchase', models.ForeignKey(db_column='purchase_idpurchase', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.purchase')),
                ('raw_material_idraw_material', models.ForeignKey(db_column='raw_material_idraw_material', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.rawmaterial')),
            ],
            options={
                'db_table': 'purchase_raw_material',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier_idsupplier',
            field=models.ForeignKey(db_column='supplier_idsupplier', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.supplier'),
        ),
    ]