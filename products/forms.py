from django import forms
from .models import OrderNow, It, Application
from .models import LEVEL, COURSE, DURATION, QUALIFICATIONS,JOB_TITLE, CGPA


GENDER = (('Choose...', 'Choose....'), ('MALE', 'Male'), ('FEMALE', 'Female'))
STATE = (('Choose...', 'Choose...'),('ab', 'Abia'), ('ada', 'Adamawa'), ('aks', 'Akwa Ibom'), ('bau', 'Bauchi'), ('bay', 'Bayelsa'), ('ben', 'Benue'), ('bor', 'Borno'),
         ('crs', 'Cross River'), ('del', 'Delta'), ('ebo', 'Ebonyi'), ('Ed', 'Edo'), ('Eki', 'Ekiti'), ('Enu', 'Enugu'), ('Gom', 'Gombe'),
         ('Im','Imo'), ('Jiga', 'Jigawa'), ('Kadu', 'Kaduna'), ('Kan', 'Kano'), ('Kat', 'Katsina'), ('Keb', 'Kebbi'), ('Kog', 'Kogi'),
         ('Kwa', 'Kwara'), ('Lag', 'Lagos'), ('Nasa', 'Nasarawa'), ('Nig', 'Niger'), ('Ogu', 'Ogun'), ('Ond', 'Ondo'), ('Osu', 'Osun'),
         ('Oy', 'Oyo'), ('Pla', 'Plateau'), ('Rs', 'Rivers'), ('Sok', 'Sokoto'), ('Tara', 'Taraba'), ('Yob', 'Yobe'),
         ('Zamfa', 'Zamfara'), ('FCT', 'Abuja'))
PRODUCTS = (('Choose...', 'Choose...'), ('AI ECOMMERCE', 'AI Ecommerce Software'), ('AI HEALTH', 'AI Healthcare Software'),
          ('AI FINANCE', 'AI Finance Software'), ('ROBOTIC', 'Robotics'), ('IMAGE RECOG.', 'Image Recognition Software'), ('CHATBOT', 'Chatterbot'),
          ('AI MARKETING', 'AI Marketing Software'), ('RESEARCH', 'Research Project'), ('WEBSITE', 'Responsive Websites'))


class OrderForm(forms.ModelForm):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(
        attrs={"class": "form-control", 'placeholder': 'register@email.com'}))
    name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control",
                                                                                                'placeholder': 'Name in full'}))
    phone = forms.CharField(label="Phone Number", max_length=11, widget=forms.NumberInput(
            attrs={"class": "form-control", 'placeholder': '+2349011914759'}))
    contact_address = forms.CharField(label="Residence Address", max_length=100, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': 'Home Address'}))
    gender = forms.ChoiceField(label='Gender', choices=GENDER, widget=forms.Select(attrs={"class": "form-control",
                                                                                          'placeholder': 'Choose gender'}))
    LGA = forms.CharField(label="LGA of Residence", max_length=50, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': 'LGA of Residence'}))
    state = forms.ChoiceField(label="State of Residence", choices=STATE, widget=forms.Select(
            attrs={"class": "form-control", 'placeholder': 'State of Origin'}))
    order = forms.ChoiceField(label="Choose Product for order", choices=PRODUCTS, widget=forms.Select(
        attrs={"class": "form-control", 'placeholder': 'Choose Product for order'}))

    class Meta:
        model = OrderNow
        fields = '__all__'


class ItForm(forms.ModelForm):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(
        attrs={"class": "form-control", 'placeholder': 'register@email.com'}))
    full_name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control",
                                                                                                'placeholder': 'SURNAME, Other names'}))
    phone = forms.CharField(label="Phone Number", max_length=11, widget=forms.NumberInput(
            attrs={"class": "form-control", 'placeholder': '+2349011914759'}))
    contact_address = forms.CharField(label="Residence Address", max_length=100, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': 'Home Address'}))
    gender = forms.ChoiceField(label='Gender', choices=GENDER, widget=forms.Select(attrs={"class": "form-control",
                                                                                          'placeholder': 'Choose gender'}))
    LGA = forms.CharField(label="LGA of Residence", max_length=50, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': 'LGA of Residence'}))
    nationality = forms.CharField(label="Nationality", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Nationality'}))
    state = forms.ChoiceField(label="State of Residence", choices=STATE, widget=forms.Select(
            attrs={"class": "form-control", 'placeholder': 'State of Origin'}))
    field_of_internship = forms.ChoiceField(label="Select field of Internship", choices=COURSE, widget=forms.Select(
        attrs={"class": "form-control", 'placeholder': 'Select field of Internship'}))
    name_of_institude = forms.CharField(label="Name of Institution", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Name of Institution'}))
    dept = forms.CharField(label="Department", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Department'}))
    faculty = forms.CharField(label="Faculty", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Faculty'}))
    level = forms.ChoiceField(label="Current Level", choices=LEVEL, widget=forms.Select(
        attrs={"class": "form-control", 'placeholder': 'Level'}))
    cgpa = forms.ChoiceField(label="Choose CGPA range", choices=CGPA, widget=forms.Select(
        attrs={"class": "form-control", 'placeholder': 'Choose CGPA range...'}))
    matric_no = forms.CharField(label="Matriculation Number", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': '21/EG/ME/001'}))
    duration = forms.ChoiceField(label="Internship Duration", choices=DURATION, widget=forms.Select(
        attrs={"class": "form-control", 'placeholder': 'Internship Duration'}))

    class Meta:
        model = It
        exclude = ['passport']
        fields = '__all__'


class ApplicationForm(forms.ModelForm):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(
        attrs={"class": "form-control", 'placeholder': 'apply@email.com'}))
    full_name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control",
                                                                                                'placeholder': 'SURNAME, Other names'}))
    phone = forms.CharField(label="Phone Number", max_length=11, widget=forms.NumberInput(
            attrs={"class": "form-control", 'placeholder': '+2349011914759'}))
    contact_address = forms.CharField(label="Residence Address", max_length=100, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': 'Home Address'}))
    gender = forms.ChoiceField(label='Gender', choices=GENDER, widget=forms.Select(attrs={"class": "form-control",
                                                                                          'placeholder': 'Choose gender'}))
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYY-MM-DD'}))
    LGA = forms.CharField(label="LGA of Origin", max_length=50, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': 'LGA of Residence'}))
    state = forms.ChoiceField(label="State of Origin", choices=STATE, widget=forms.Select(
            attrs={"class": "form-control", 'placeholder': 'State of Origin'}))
    educational_qualification = forms.ChoiceField(label="Qualification", choices=QUALIFICATIONS, widget=forms.Select(
        attrs={"class": "form-control", 'placeholder': 'Select Highest Qualification attended'}))
    jod_title = forms.ChoiceField(label="Job Title", choices=JOB_TITLE, widget=forms.Select(
        attrs={"class": "form-control", 'placeholder': 'Job Apply for'}))
    # resume = forms.FileField(label="Upload your Resume", widget=forms.FileInput(
    #     attrs={'placeholder': 'Upload Resume'}))

    class Meta:
        model = Application
        fields = '__all__'

