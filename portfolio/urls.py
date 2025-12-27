from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ← Важно: name='home'
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
