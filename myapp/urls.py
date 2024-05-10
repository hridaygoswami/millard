from django.urls import path 
from . import views

app_name = "myapp"
urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("menu/", views.menu, name='menu'),
    path("reservations/", views.reservations, name='reservations'),
    path("feedback/", views.feedback, name='feedback'),
    path("redirect_reservation/", views.redirect_reservations, name='redirect_reservations'),
    path("redirect_feedback/", views.redirect_feedback, name='feedback_redirect')
]