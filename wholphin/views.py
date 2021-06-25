from email import message
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from products.models import Products
from .models import Courses, CoursesDetail, UsersComment, StudentRegistered, Carousel
from .forms import UsersCommentForm, RegisterForm
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage


class Home(ListView):
    model = Courses
    context = Products
    comment = UsersCommentForm
    template_name = 'wholphin/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['course1'] = Courses.objects.all()[:4]
        context['service'] = Products.objects.all()[:4]
        context['comment'] = UsersComment.objects.all()
        context['car'] = Carousel.objects.all()
        return context


class HomePage(ListView):
    model = Courses
    context = Products
    comment = UsersCommentForm
    template_name = 'wholphin/homepage.html'


    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['course1'] = Courses.objects.all()[:4]
        context['service'] = Products.objects.all()[:4]
        context['comment'] = UsersComment.objects.all()
        return context



#@login_required(login_url='wholphin:home')
def about(request):
    return render(request, 'wholphin/about.html')


def contact(request):
    return render(request, 'wholphin/contact.html')


def terms(request):
    return render(request, 'wholphin/terms.html')


# def register_view(request):
#     form = RegisterForm
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             h = 'We appreciate your effort to comment, its important to us'
#             messages.add_message(request, messages.SUCCESS, h)
#             return HttpResponseRedirect(reverse('wholphin:home'))
#     return render(request, 'wholphin/register.html', {'form': form})


class CourseHome(ListView):
    model = Courses
    #queryset = Courses.objects.all()[:4]
    #context_object_name = 'courses'
    template_name = 'wholphin/courses.html'

    def get_context_data(self, **kwargs):
        context = super(CourseHome, self).get_context_data(**kwargs)
        context['course1'] = Courses.objects.all()[:4]
        context['course2'] = Courses.objects.all()[4:7]
        #context['course3'] = Courses.objects.all()[7:9]
        context['course4'] = Courses.objects.all()[7:9]
        context['course5'] = Courses.objects.all()[14:18]
        context['course6'] = Courses.objects.all()[18:22]
        return context


class CourseDetail(DetailView):
    model = Courses
    context_object_name = 'price'
    template_name = 'wholphin/coursesprice.html'


class Course_Apply(DetailView):
    model = CoursesDetail
    template_name = 'wholphin/courseapply.html'
    context_object_name = 'apply'


def services(request):
    return render(request, 'wholphin/services.html')

#
# def lay(request):
#     return render(request, 'layout.html')


def feedback_view(request):
    form = UsersCommentForm
    if request.method == 'POST':
        form = UsersCommentForm(request.POST)
        if form.is_valid():
            form.save()
            h = 'We appreciate your effort to comment, its important to us'
            messages.add_message(request, messages.SUCCESS, h)
            return HttpResponseRedirect(reverse('wholphin:home'))
    return render(request, 'wholphin/feedback.html', {'form': form})


def register_view(request):
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # h = 'You have successfully registered for a course'
            # messages.add_message(request, messages.SUCCESS, h)
            return HttpResponseRedirect(reverse('wholphin:register_success'))
    return render(request, 'wholphin/register.html', {'form': form})


def register_success(request):

    return render(request, 'wholphin/register_success.html')


def register_form_vew(request):
    context = StudentRegistered.objects.all()[:3]
    return render(request, 'wholphin/printform.html', {'context': context})
