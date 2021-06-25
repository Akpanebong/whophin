# Generated by Django 3.1b1 on 2021-05-12 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_productdetail_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderNow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('contact_address', models.CharField(max_length=200)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('Choose...', 'Choose....'), ('MALE', 'Male'), ('FEMALE', 'Female')], max_length=20)),
                ('state', models.CharField(choices=[('ab', 'Abia'), ('ada', 'Adamawa'), ('aks', 'Akwa Ibom'), ('bau', 'Bauchi'), ('bay', 'Bayelsa'), ('ben', 'Benue'), ('bor', 'Borno'), ('crs', 'Cross River'), ('del', 'Delta'), ('ebo', 'Ebonyi'), ('Ed', 'Edo'), ('Eki', 'Ekiti'), ('Enu', 'Enugu'), ('Gom', 'Gombe'), ('Im', 'Imo'), ('Jiga', 'Jigawa'), ('Kadu', 'Kaduna'), ('Kan', 'Kano'), ('Kat', 'Katsina'), ('Keb', 'Kebbi'), ('Kog', 'Kogi'), ('Kwa', 'Kwara'), ('Lag', 'Lagos'), ('Nasa', 'Nasarawa'), ('Nig', 'Niger'), ('Ogu', 'Ogun'), ('Ond', 'Ondo'), ('Osu', 'Osun'), ('Oy', 'Oyo'), ('Pla', 'Plateau'), ('Rs', 'Rivers'), ('Sok', 'Sokoto'), ('Tara', 'Taraba'), ('Yob', 'Yobe'), ('Zamfa', 'Zamfara'), ('FCT', 'Abuja')], max_length=30)),
                ('LGA', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Product Ordered',
            },
        ),
    ]
