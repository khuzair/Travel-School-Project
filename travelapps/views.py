from multiprocessing import context
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomLoginForm, CustomBookingForm
from .models import TourDestination, NewTourDestination


def booking(request):
    form = CustomBookingForm()
    if request.method == "POST":
        form = CustomBookingForm(request.POST)
        your_name = request.POST['full_name']
        your_email = request.POST['email']
        your_phone = request.POST['phone']
        visit_date = request.POST['visit_date']
        num_of_pass = request.POST['num_of_pass']
        query = request.POST['query']
        return render(request, 'registrations/booking-confirmation.html', {
            'your_name': your_name,
            'your_email': your_email,
            'your_phone': your_phone,
            'visit_date': visit_date,
            'num_of_pass': num_of_pass,
            'query': query
        })
    context = {
        'form': form
    }
    return render(request, "registrations/booking.html", context)
    

def booking_confirmation(request):
    return render(request, "registrations/booking-confirmation.html")       


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'the new user {username} has been created')
                return redirect('login')

        context = {
            "form": form
        }
        return render(request, 'registrations/signup.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            form = CustomLoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                raw_pswd = form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_pswd)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        form  = CustomLoginForm()
        return render(request, 'registrations/login.html', {"form": form})

def logoutPage(request):
    logout(request)
    return redirect('/')


def landing_page(request):
    new_destination = NewTourDestination.objects.all()
    context = {
        'city': new_destination
    }
    return render(request, 'index.html', context)


def about_us(request):
    return render(request, 'about-us.html')


def contact(request):
    return render(request, 'contact.html')


def customer_protection(request):
    return render(request, 'customer-protection.html')


def our_offer(request):
    destination = TourDestination.objects.all()
    context = {
        'city': destination
    }
    return render(request, 'our-offer.html', context)
