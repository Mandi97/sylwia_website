from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('o-mnie', views.AboutMe.as_view(), name='o-mnie'),
    path('kontakt', views.Contact.as_view(), name='kontakt'),
]
