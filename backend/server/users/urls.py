from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('dashboard/',views.dashboardView,name="dashboard"),
    path('register/',views.registerView,name='register_url'),
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login_url'),
    path('logout/',LogoutView.as_view(next_page='home-page'),name='logout'),
]