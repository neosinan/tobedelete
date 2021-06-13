from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.homepage, name="homepage"),

]
