from django import forms
from .models import UsersComment, StudentRegistered, Courses


class UsersCommentForm(forms.ModelForm):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder':'comment@gmail.com'}))
    name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Name, start with surname'}))
    suggestion = forms.CharField(label='Comment', max_length=2000, widget=forms.Textarea(attrs={'class': "form-control", 'placeholder':'Drop your comment here'}))

    class Meta:
        model = UsersComment
        fields = '__all__'


GENDER = (('Choose...', 'Choose....'), ('MALE', 'Male'), ('FEMALE', 'Female'))
COURSE = (('Choose...', 'Choose...'), ('AI', 'Artificial Intelligence'), ('WB', 'Web Development'),
          ('ML', 'Machine Learning'), ('DL', 'Deep Learning'), ('RB', 'Robotics'), ('APP', 'App Development'),
          ('CP', 'Computer Programming'), ('GD', 'Graphic Design'), ('WP', 'Word Processing'))
STATE = (('Choose...', 'Choose...'),('ab', 'Abia'), ('ada', 'Adamawa'), ('aks', 'Akwa Ibom'), ('bau', 'Bauchi'), ('bay', 'Bayelsa'), ('ben', 'Benue'), ('bor', 'Borno'),
         ('crs', 'Cross River'), ('del', 'Delta'), ('ebo', 'Ebonyi'), ('Ed', 'Edo'), ('Eki', 'Ekiti'), ('Enu', 'Enugu'), ('Gom', 'Gombe'),
         ('Im','Imo'), ('Jiga', 'Jigawa'), ('Kadu', 'Kaduna'), ('Kan', 'Kano'), ('Kat', 'Katsina'), ('Keb', 'Kebbi'), ('Kog', 'Kogi'),
         ('Kwa', 'Kwara'), ('Lag', 'Lagos'), ('Nasa', 'Nasarawa'), ('Nig', 'Niger'), ('Ogu', 'Ogun'), ('Ond', 'Ondo'), ('Osu', 'Osun'),
         ('Oy', 'Oyo'), ('Pla', 'Plateau'), ('Rs', 'Rivers'), ('Sok', 'Sokoto'), ('Tara', 'Taraba'), ('Yob', 'Yobe'),
         ('Zamfa', 'Zamfara'), ('FCT', 'Abuja'))


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(
        attrs={"class": "form-control", 'placeholder': 'register@email.com'}))

    surname = forms.CharField(label="Surname", max_length=50, widget=forms.TextInput(attrs={"class": "form-control",
                                                                                                'placeholder': 'Surname'}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': 'First Name'}))
    other_name = forms.CharField(label="Other Name", max_length=50, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': 'Other Names'}))
    phone_number = forms.CharField(label="Phone Number", max_length=50, widget=forms.NumberInput(
            attrs={"class": "form-control", 'placeholder': '+2349011914759'}))
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(
            attrs={"class": "form-control", 'placeholder': 'YYY-MM-DD'}))
    home_address = forms.CharField(label="Home Address", max_length=100, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': 'Home Address'}))
    contact_address = forms.CharField(label="Contact Address", max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Contact Address'}))
    LGA_of_origin = forms.CharField(label="LGA of Origin", max_length=50, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': 'LGA of Origin'}))
    state_of_origin = forms.ChoiceField(label="State of Origin", choices=STATE, widget=forms.Select(
            attrs={"class": "form-control", 'placeholder': 'State of Origin'}))
    Gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(attrs={"class": "form-control",
                                                                          'placeholder': 'Choose gender'}))
    course = forms.ChoiceField(label="Course", choices=COURSE, widget=forms.Select(attrs={"class": "form-control"}))
    t_and_c = forms.BooleanField(label="Terms and Conditions",required=True)

    class Meta:
        model = StudentRegistered
        fields = '__all__'
