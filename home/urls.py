from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import RegistrationView, VerificationView

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('about/', views.about, name='about'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),

]
