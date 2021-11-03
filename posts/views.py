from django.contrib.auth import login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DetailView

from posts.forms import RegisterForm, LoginForm, PostForm, ProfileForm
from posts.models import Posts, Profile, Role
from posts.utils import DataMixin


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        profile = Profile.objects.create(user=user, role=Role.objects.filter(title='Читатель').first())
        profile.save()
        login(self.request, user)
        return redirect('main')


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def logout_user(request):
    logout(request)
    return redirect('login')


class ProfileView(DataMixin, UpdateView):
    model = Profile
    template_name = 'profile.html'
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class MainView(DataMixin, CreateView):
    form_class = PostForm
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Posts.objects.all().order_by('-created_at')
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return redirect('main')


class PostView(DataMixin, DetailView):
    template_name = 'discussion.html'
    model = Posts
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

