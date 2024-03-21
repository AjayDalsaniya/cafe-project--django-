# Generated by Django 4.1.3 on 2023-02-01 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0065_alter_order_order_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablereservation',
            name='table_reservation_time',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.CreateModel(
            name='TableReservationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_idtable', models.ForeignKey(db_column='table_idtable', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.table')),
                ('table_reservation_idtable_reservation', models.ForeignKey(db_column='table_reservation_idtable_reservation', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.tablereservation')),
            ],
            options={
                'db_table': 'table_reservation_details',
                'managed': True,
            },
        ),
    ]
