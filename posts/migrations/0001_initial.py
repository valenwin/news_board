# Generated by Django 3.0.6 on 2020-05-15 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("author_name", models.CharField(max_length=200)),
                ("link", models.URLField(max_length=1000)),
                ("upvotes", models.PositiveIntegerField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("update", models.DateField(auto_now=True)),
            ],
            options={"ordering": ("-created",),},
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author_name", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="posts.Post",
                    ),
                ),
            ],
            options={"ordering": ("-created",),},
        ),
    ]
