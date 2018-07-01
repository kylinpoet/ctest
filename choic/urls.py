from django.urls import path
from choic import views

app_name = 'choic'
urlpatterns = [

    path('',views.index),
    path('answer/',views.answer),
    path('saveresult/',views.saveresult,name='saveresult'),
    path('loginstu/',views.loginstu),
    path('logoutstu/',views.logoutstu),

]