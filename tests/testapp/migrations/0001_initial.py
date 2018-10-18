# Generated by Django 2.1.2 on 2018-10-16 19:46
import jsonfallback.fields
from django.core.serializers.json import DjangoJSONEncoder
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', jsonfallback.fields.FallbackJSONField(
                    encoder=DjangoJSONEncoder, null=False, default={'foo': 'bar'}
                )),
            ],
        ),
    ]
