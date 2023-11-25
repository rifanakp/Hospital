# Generated by Django 4.1.3 on 2023-11-22 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haritha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=50)),
                ('doc_image', models.ImageField(upload_to='images')),
                ('doc_dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haritha.department')),
            ],
        ),
    ]
