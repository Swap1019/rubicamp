import os
from django.shortcuts import HttpResponseRedirect,render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from .forms import (
    SignUpForm,
    UserInfoForm
    )
from .models import (
    UserInfo
)
from django.views.generic import (
    CreateView,
    TemplateView,
    View,
    )
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from .mixins import UserWebsiteOwnerMixin


class HomeView(TemplateView):
    template_name = 'rubikamp/home.html'

class WebsiteCreateView(LoginRequiredMixin,TemplateView):
    template_name = 'rubikamp/create-website.html'

class AboutView(TemplateView):
    template_name = 'rubikamp/about.html'

class UserCongratulations(UserWebsiteOwnerMixin,LoginRequiredMixin,TemplateView):
    template_name = 'rubikamp/congratulations.html'
    

class UserGeneratedWebsiteView(UserWebsiteOwnerMixin,LoginRequiredMixin,TemplateView):
    template_name = 'generated-website/index.html'

class RedirectView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        
        if request.user.is_ownwebsite:
            return redirect('rubikamp:user-website-generated')

        return redirect('rubikamp:user-website-create')

STEP_FIELDS = [
    'website_type',
    'user_type',
    'extra_features',
    'sample',
    'color_palette',
    'logo',
    'text_content'
]

class UserInfoCreateView(LoginRequiredMixin, View):
    template_name = 'rubikamp/user-info-form.html'
    success_url = reverse_lazy('rubikamp:user-website-congratulations')

    def get(self, request, *args, **kwargs):
        step = int(request.GET.get('step', 1))
        field = STEP_FIELDS[step - 1]
        form = UserInfoForm(fields=[field])
        return self.render_step(request, form, step)

    def post(self, request, *args, **kwargs):
        step = int(request.POST.get('step', 1))
        field = STEP_FIELDS[step - 1]
        form = UserInfoForm(request.POST, request.FILES, fields=[field])
        user = request.user

        if form.is_valid():
            # Save current field data to session
            if field == 'logo':
                # Don't store file in session
                request.session[f'user_info_step_{step}'] = {}  # Or just skip this line entirely
            else:
                request.session[f'user_info_step_{step}'] = form.cleaned_data

            if step < len(STEP_FIELDS):
                return redirect(f'{request.path}?step={step + 1}')
            else:
                # Final step: gather all session data
                combined_data = {}
                for i in range(len(STEP_FIELDS)):
                    combined_data.update(request.session.get(f'user_info_step_{i+1}', {}))
                final_form = UserInfoForm(combined_data, request.FILES)
                if final_form.is_valid():
                    user_info = final_form.save(commit=False)
                    user_info.user = request.user
                    user_info.save()
                    user.is_ownwebsite = True
                    user.save()

                    # Clean up session
                    for i in range(len(STEP_FIELDS)):
                        request.session.pop(f'user_info_step_{i+1}', None)

                    return redirect(self.success_url)

        return self.render_step(request, form, step)

    def render_step(self, request, form, step):
        context = {
            'form': form,
            'step': step,
            'fields': STEP_FIELDS
        }
        return render(request, self.template_name, context)



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