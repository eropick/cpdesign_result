# Generated by Django 5.0.3 on 2024-05-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeshare', '0003_alter_document_unique_together_remove_document_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='doc_type',
            field=models.CharField(default='default', max_length=30),
        ),
    ]
