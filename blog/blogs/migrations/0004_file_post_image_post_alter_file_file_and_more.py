# Generated by Django 5.2 on 2025-04-09 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0003_alter_file_file_alter_image_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="post",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="blogs.post"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="image",
            name="post",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="blogs.post"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(upload_to="otherfiles/"),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
