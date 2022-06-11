from django.urls import path

from . import views

urlpatterns = [
    path('get-projects/', views.index, name='index'),
    path('contact-me/', views.contactMe, name='contactMe'),
]