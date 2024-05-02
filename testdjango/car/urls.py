from django.urls import path
from . import views

app_name = "car"
urlpatterns = [
    path('', views.info,name='homepage'),
    path('add', views.add, name='add'),

]
