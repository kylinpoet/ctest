from django.urls import path
from choic import views

app_name = 'choic'
urlpatterns = [

    path('',views.index),
    path('saveresult/',views.saveresult),
    path('loginstu/',views.loginstu),


]