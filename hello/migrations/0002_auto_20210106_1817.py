
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=120, null=True)),
                ('address2', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('state', models.CharField(max_length=11, null=True)),
                ('zip', models.CharField(max_length=11, null=True)),
                ('comments', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
