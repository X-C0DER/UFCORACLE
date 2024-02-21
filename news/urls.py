from django.urls import path 
from . import views


urlpatterns = [
        path('', views.index, name="Index"),
        path ('news',views.news,name="News"),
        path ('events',views.events,name="Events"),
        path ('oracle',views.oracle,name="Oracle")
    ]