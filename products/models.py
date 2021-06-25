from django.db import models

# Create your models here.
from django.urls import reverse
QUALIFICATIONS = (('Choose...', 'Choose...'),('Ssce', 'SSCE'), ('Nd', 'ND'), ('Hnd', 'HND'), ('BSc', 'BSc/BEng'), ('MASTERS', 'Masters'))
JOB_TITLE = (('Choose...', 'Choose...'),('PHPWEB', 'PHP Web Developer'), ('DJANGOWEB', 'Django Web Developer'), ('APP DEVELOPER', 'App Developer'),
             ('SOFTWARE DEVELOPER', 'Software Developer'), ('AI DEVELOPER', 'Artificial Intelligent Engineer'), ('ELECT/ELECT', 'Electrical/Electronic Engineer'),
             ('RECEPTIONIST', 'Receptionist'), ('DATA_SCIENTIST', 'Data Scientist'), ('FRONT_END_DEV.', 'Front End Developer'), ('MACHINE LEARNING ENGR,', 'Machine Learning Engineer'),
             ('PYTHON_DEV', 'Python Developer'))

GENDER = (('Choose...', 'Choose....'), ('MALE', 'Male'), ('FEMALE', 'Female'))
LEVEL = (('Choose...', 'Choose....'), ('300L', '300 Level'), ('400L', '400 Level'), ('Nd', 'ND'), ('Hnd', 'HND'))
DURATION = (('Choose...', 'Choose....'), ('3M', '3 Months'), ('6M', '6 Months'), ('12M', '12 Months'))
STATE = (('Choose...', 'Choose...'),('ab', 'Abia'), ('ada', 'Adamawa'), ('aks', 'Akwa Ibom'), ('bau', 'Bauchi'), ('bay', 'Bayelsa'), ('ben', 'Benue'), ('bor', 'Borno'),
         ('crs', 'Cross River'), ('del', 'Delta'), ('ebo', 'Ebonyi'), ('Ed', 'Edo'), ('Eki', 'Ekiti'), ('Enu', 'Enugu'), ('Gom', 'Gombe'),
         ('Im','Imo'), ('Jiga', 'Jigawa'), ('Kadu', 'Kaduna'), ('Kan', 'Kano'), ('Kat', 'Katsina'), ('Keb', 'Kebbi'), ('Kog', 'Kogi'),
         ('Kwa', 'Kwara'), ('Lag', 'Lagos'), ('Nasa', 'Nasarawa'), ('Nig', 'Niger'), ('Ogu', 'Ogun'), ('Ond', 'Ondo'), ('Osu', 'Osun'),
         ('Oy', 'Oyo'), ('Pla', 'Plateau'), ('Rs', 'Rivers'), ('Sok', 'Sokoto'), ('Tara', 'Taraba'), ('Yob', 'Yobe'),
         ('Zamfa', 'Zamfara'), ('FCT', 'Abuja'))
PRODUCTS = (('Choose...', 'Choose...'), ('AI ECOMMERCE', 'AI Ecommerce Software'), ('AI HEALTH', 'AI Healthcare Software'),
          ('AI FINANCE', 'AI Finance Software'), ('ROBOTIC', 'Robotics'), ('IMAGE RECOG.', 'Image Recognition Software'), ('CHATBOT', 'Chatterbot'),
          ('AI MARKETING', 'AI Marketing Software'), ('RESEARCH', 'Research Project'), ('WEBSITE', 'Responsive Websites'))
from wholphin.models import COURSE
CGPA = (('choose...', 'choose CGPA range...'), ('first class', '4.50 - 5.00'),
        ('second class upper', '3.50 - 4.49'),('second class lower', '2.50 - 3.49'),
        ('others', '1.00 - 2.49'))

class Products(models.Model):
    service_rendered = models.CharField(max_length=100)
    pics = models.ImageField(upload_to='picture')
    description = models.TextField()

    def __str__(self):
        return f'{self.service_rendered}'

    def get_absolute_url(self):
        return reverse('wholphinplus:productdetail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Products"


class ProductDetail(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product} cost {self.price}'

    class Meta:
        verbose_name_plural = "ProductDetail"

    def get_absolute_url(self):
        return reverse('wholphin:productdetail', kwargs={'pk': self.pk})


class OrderNow(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    contact_address = models.CharField(max_length=200)
    date_ordered = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    state = models.CharField(max_length=30, choices=STATE)
    LGA = models.CharField(max_length=30)
    order = models.CharField(max_length=30, choices=PRODUCTS)

    def __str__(self):
        return f'{self.name} with the email: {self.email} ordered for {self.order} on {self.date_ordered}'

    class Meta:
        verbose_name_plural = "Product Ordered"


class It(models.Model):
    passport = models.ImageField(upload_to='IT', blank=True, null=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    contact_address = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER)
    state = models.CharField(max_length=30, choices=STATE)
    LGA = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    field_of_internship = models.CharField(max_length=100, choices=COURSE)
    name_of_institude = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    level = models.CharField(max_length=30, choices=LEVEL)
    cgpa = models.CharField(max_length=30, choices=CGPA)
    matric_no = models.CharField(max_length=20)
    duration = models.CharField(max_length=20, choices=DURATION)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} with {self.phone} of {self.name_of_institude} registered for {self.field_of_internship} Internship on {self.date_registered}'

    class Meta:
        verbose_name_plural = "Interns"


class Application(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    contact_address = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER)
    dob = models.DateField()
    state = models.CharField(max_length=30, choices=STATE)
    LGA = models.CharField(max_length=30)
    educational_qualification = models.CharField(max_length=100, choices=QUALIFICATIONS)
    jod_title = models.CharField(max_length=100, choices=JOB_TITLE)
    # resume = models.FileField(upload_to='Resumes')
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} with {self.phone} of {self.state} state applied as {self.jod_title} on {self.date_registered}'

    class Meta:
        verbose_name_plural = "Job Application"
