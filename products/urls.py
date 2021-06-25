from django.urls import path
from .views import ProductDetailView, ProductView, order, get_started, eportal, it_view, ai_view, it_success, application_view, it_manual_view, product_success_view

app_name = 'wholphinplus'

urlpatterns = [
    path('', ProductView.as_view(), name='products'),
    path('<int:pk>/', ProductDetailView.as_view(), name='productdetail'),
    path('order/', order, name='order'),
    path('get{}started/', get_started, name='get started'),
    path('eportal/', eportal, name='eportal'),
    path('AI/', ai_view, name='AI'),
    path('it1/', it_view, name='it1'),
    path('it1l/', it_manual_view, name='it1l'),
    path('it_success/', it_success, name='it_success'),
    path('application/', application_view, name='application'),
    path('order_success/', product_success_view, name='order_success'),
]
