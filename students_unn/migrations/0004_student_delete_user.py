# Generated by Django 5.0.2 on 2024-03-04 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_unn', '0003_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('reg_no', models.PositiveIntegerField()),
                ('dept', models.CharField(max_length=100)),
                ('level', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('UG', 'UNDERGRADUATE'), ('PG', 'POSTGRADUATE'), ('SD', 'SANDWICH')], default='UG', max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
