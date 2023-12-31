# Generated by Django 4.2.6 on 2023-11-30 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_user_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(default="Shootersrev12#", upload_to=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(default="Shootersrev12"),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("media", models.ImageField(upload_to="")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
        ),
    ]
