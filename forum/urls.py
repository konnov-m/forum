from django.contrib import admin
from django.urls import path

from posts.views import RegisterView, LoginView, MainView, ProfileView, logout_user, PostView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('post/<slug:slug>', PostView.as_view(), name='post'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile')
]