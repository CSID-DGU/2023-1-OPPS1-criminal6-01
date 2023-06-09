# Generated by Django 4.2.2 on 2023-06-17 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AppUser",
            fields=[
                ("userID", models.AutoField(primary_key=True, serialize=False)),
                ("id", models.CharField(max_length=45, unique=True)),
                ("password", models.CharField(max_length=45)),
                ("name", models.CharField(default="", max_length=45)),
                ("roomID", models.CharField(default="", max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                ("roomID", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(default="", max_length=45)),
                ("roomIntro", models.TextField(max_length=200, null=True)),
                ("date", models.CharField(max_length=45)),
                ("region", models.CharField(default="", max_length=45)),
                ("genre", models.IntegerField(default=0)),
                ("difficulty", models.FloatField(default=0)),
                ("fear", models.FloatField(default=0)),
                ("activity", models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Chat",
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
                ("chatID", models.IntegerField()),
                ("content", models.TextField()),
                ("createAT", models.DateTimeField()),
                (
                    "roomId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chats",
                        to="c6_app.room",
                    ),
                ),
                (
                    "senderID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chats",
                        to="c6_app.appuser",
                    ),
                ),
            ],
        ),
    ]
