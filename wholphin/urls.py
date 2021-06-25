from django.urls import path
from .views import Home, about, HomePage, CourseHome, services, register_form_vew, CourseDetail, Course_Apply, feedback_view, register_view, contact,terms, register_success

app_name = 'wholphin'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('h/', HomePage.as_view(), name='homepage'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('courses/', CourseHome.as_view(), name='course'),
    path('<int:pk>/', CourseDetail.as_view(), name='courseprice'),
    path('<int:courses_id>/<int:pk>/', Course_Apply.as_view(), name='apply'),
    path('feedback/', feedback_view, name='feedback'),
    path('contact/', contact, name='contact'),
    path('register/', register_view, name='register'),
    path('t&c/', terms, name='t&c'),
    #path('lay', lay, name='lay'),
    path('register_success/', register_success, name='register_success'),
    path('registered/', register_form_vew, name='registered'),
]
