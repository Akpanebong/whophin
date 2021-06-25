# Generated by Django 3.1b1 on 2021-06-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210513_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='It',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('contact_address', models.CharField(max_length=200)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('Choose...', 'Choose....'), ('MALE', 'Male'), ('FEMALE', 'Female')], max_length=20)),
                ('state', models.CharField(choices=[('ab', 'Abia'), ('ada', 'Adamawa'), ('aks', 'Akwa Ibom'), ('bau', 'Bauchi'), ('bay', 'Bayelsa'), ('ben', 'Benue'), ('bor', 'Borno'), ('crs', 'Cross River'), ('del', 'Delta'), ('ebo', 'Ebonyi'), ('Ed', 'Edo'), ('Eki', 'Ekiti'), ('Enu', 'Enugu'), ('Gom', 'Gombe'), ('Im', 'Imo'), ('Jiga', 'Jigawa'), ('Kadu', 'Kaduna'), ('Kan', 'Kano'), ('Kat', 'Katsina'), ('Keb', 'Kebbi'), ('Kog', 'Kogi'), ('Kwa', 'Kwara'), ('Lag', 'Lagos'), ('Nasa', 'Nasarawa'), ('Nig', 'Niger'), ('Ogu', 'Ogun'), ('Ond', 'Ondo'), ('Osu', 'Osun'), ('Oy', 'Oyo'), ('Pla', 'Plateau'), ('Rs', 'Rivers'), ('Sok', 'Sokoto'), ('Tara', 'Taraba'), ('Yob', 'Yobe'), ('Zamfa', 'Zamfara'), ('FCT', 'Abuja')], max_length=30)),
                ('LGA', models.CharField(max_length=30)),
                ('field_of_internship', models.CharField(choices=[('Choose...', 'Choose...'), ('AI', 'Artificial Intelligence'), ('WB', 'Web Development'), ('ML', 'Machine Learning'), ('DL', 'Deep Learning'), ('RB', 'Robotics'), ('APP', 'App Development'), ('CP', 'Computer Programming'), ('GD', 'Graphic Design'), ('WP', 'Word Processing')], max_length=100)),
                ('name_of_institude', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('Choose...', 'Choose....'), ('300L', '300 Level'), ('400L', '400 Level')], max_length=30)),
                ('cgpa', models.PositiveIntegerField()),
                ('matric_no', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField()),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Interns',
            },
        ),
    ]
