from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .forms import OrderForm, ItForm, ApplicationForm
from products.models import Products


class ProductView(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'products/products.html'


class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'pro'
    template_name = 'products/productdetail.html'


def order(request):
    form = OrderForm
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('wholphinplus:order_success'))
    return render(request, 'products/order.html', {'form': form})


def get_started(request):
    return render(request, 'products/get_started.html')


def eportal(request):
    return render(request, 'products/eportal.html')


def it_view(request):
    form = ItForm
    if request.method == 'POST':
        form = ItForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('wholphinplus:it1l'))
    return render(request, 'products/it.html', {'form': form})


def it_success(request):
    return render(request, 'products/it_success.html')


def it_manual_view(request):
    m = 'Your IT Application has been received successfully, ensure to print and fill the form below and submit it at the office with the underlisted requirements'
    messages.add_message(request, messages.SUCCESS, m)
    return render(request, 'products/it_manual_form.html')


def application_view(request):
    form = ApplicationForm
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('wholphinplus:it_success'))
    return render(request, 'products/application.html', {'form': form})


def product_success_view(request):
    return render(request, 'products/product_form_success.html')


def ai_view(request):
    return render(request, 'products/AI.html')


def order_success(request):
    return render(request, 'products/order_success.html')

