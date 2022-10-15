from django.urls import path
from .views import landing_page, contact, about_us, customer_protection, our_offer

app_name = "travelapps"


urlpatterns = [
    path('', landing_page, name="landing-page"),
    path('about/', about_us, name="about-us"),
    path('contact/', contact, name="contact"),
    path('customer/', customer_protection, name="customer-protection"),
    path('offer/', our_offer, name="our-offer"),

]