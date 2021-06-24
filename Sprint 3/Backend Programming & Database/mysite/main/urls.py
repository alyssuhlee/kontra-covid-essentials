from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name = 'homepage'),
    path('products/', views.products, name = 'products'),
    path('ppes/', views.ppes, name = 'ppes'),
    path('disinfectants/', views.disinfectants, name = 'disinfectants'),
    path('accessories/', views.accessories, name = 'accessories'),
    path('reviews/', views.reviews, name = 'reviews'),
    path('about/', views.about, name = 'about'),
    path('queries/', views.queries, name = 'queries'),
]