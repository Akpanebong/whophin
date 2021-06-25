from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Courses(models.Model):
    course_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='picture')
    image1 = models.ImageField(upload_to='picture')
    description = models.TextField()
    duration = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.duration} months of {self.course_title} for N{self.amount}'

    def get_absolute_url(self):
        return reverse('wholphin:courseprice', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Courses'


class CoursesDetail(models.Model):
    course_subtitle = models.CharField(max_length=100)
    description = models.TextField()
    image1 = models.ImageField(upload_to='picture')
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Courses' Detail"

    def __str__(self):
        return self.course_subtitle


GENDER = (('MALE', 'Male'), ('FEMALE', 'Female'))
COURSE = (('Choose...', 'Choose...'), ('AI', 'Artificial Intelligence'), ('WB', 'Web Development'),
          ('ML', 'Machine Learning'), ('DL', 'Deep Learning'), ('RB', 'Robotics'), ('APP', 'App Development'),
          ('CP', 'Computer Programming'), ('GD', 'Graphic Design'), ('WP', 'Word Processing'))
STATE = (('Choose...', 'Choose...'),('ab', 'Abia'), ('ada', 'Adamawa'), ('aks', 'Akwa Ibom'), ('bau', 'Bauchi'), ('bay', 'Bayelsa'), ('ben', 'Benue'), ('bor', 'Borno'),
         ('crs', 'Cross River'), ('del', 'Delta'), ('ebo', 'Ebonyi'), ('Ed', 'Edo'), ('Eki', 'Ekiti'), ('Enu', 'Enugu'), ('Gom', 'Gombe'),
         ('Im','Imo'), ('Jiga', 'Jigawa'), ('Kadu', 'Kaduna'), ('Kan', 'Kano'), ('Kat', 'Katsina'), ('Keb', 'Kebbi'), ('Kog', 'Kogi'),
         ('Kwa', 'Kwara'), ('Lag', 'Lagos'), ('Nasa', 'Nasarawa'), ('Nig', 'Niger'), ('Ogu', 'Ogun'), ('Ond', 'Ondo'), ('Osu', 'Osun'),
         ('Oy', 'Oyo'), ('Pla', 'Plateau'), ('Rs', 'Rivers'), ('Sok', 'Sokoto'), ('Tara', 'Taraba'), ('Yob', 'Yobe'),
         ('Zamfa', 'Zamfara'), ('FCT', 'Abuja'))


class UsersComment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    suggestion = models.TextField()

    def __str__(self):
        return self.name


class StudentRegistered(models.Model):
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    home_address = models.CharField(max_length=100)
    contact_address = models.CharField(max_length=100)
    LGA_of_origin = models.CharField(max_length=100)
    state_of_origin = models.CharField(max_length=100, choices=STATE)
    Gender = models.CharField(max_length=7, choices=GENDER)
    course = models.CharField(max_length=100, choices=COURSE)
    t_and_c = models.BooleanField(default=False)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.surname} {self.first_name} has registered online for {self.course} on {self.date_registered}'

    class Meta:
        verbose_name_plural = "Student Registered"


class Students(models.Model):
    id = models.AutoField(primary_key=True)
   # admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    address = models.TextField()
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.address


class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel')
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.title