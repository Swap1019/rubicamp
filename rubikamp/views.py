from django.shortcuts import HttpResponseRedirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import (
    SignUpForm,
    )

from django.urls import reverse_lazy,reverse
from django.views.generic import (
    CreateView,
    TemplateView
    )
from django.contrib.auth.views import LoginView,LogoutView

class HomeView(TemplateView):
    template_name = 'rubikamp/home.html'


class RegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'rubikamp/register.html'

    def form_valid(self,form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse('rubikamp:user-login'))


class UserLoginView(LoginView):
    template_name = 'rubikamp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('rubikamp:Home')
    
class UserLogoutView(LogoutView):
    template_name = 'rubikamp/home.html'
    
    def get_success_url(self):
        return reverse_lazy('rubikamp:Home')