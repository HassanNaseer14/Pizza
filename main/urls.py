from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name="home"),
    path('menu/', v.menu, name="menu")
     
]