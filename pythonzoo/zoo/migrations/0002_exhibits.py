# Generated by Django 2.0.4 on 2018-04-25 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter an Exhibit name.', max_length=200)),
                ('zoo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zoo.Zoo')),
            ],
        ),
    ]