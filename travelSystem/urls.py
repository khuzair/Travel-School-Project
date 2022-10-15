from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from travelapps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('booking/', views.booking, name="book-tour"),
    path('booking-confirmation/', views.booking_confirmation, name="book-tour-confirmation"),
    path('', include('travelapps.urls', namespace="travelapps"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

