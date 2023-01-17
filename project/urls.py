from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.Home.as_view(), name='home'),
    path('manager/', views.ManagerDashboard.as_view(), name='manager_dashboard'),
]
