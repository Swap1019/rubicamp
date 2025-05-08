from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    )
from .models import (
    User,
    UserInfo,
    )

class SignUpForm(UserCreationForm):
    #User signup form
    email = forms.EmailField(max_length=200,required=True)
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    profile = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'id': 'id_profile'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','profile']
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password','style':'margin-bottom:7px;'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation','style':'margin-bottom:7px;'})



class UserInfoForm(forms.ModelForm):
    def __init__(self, *args, fields=None, **kwargs):
        super().__init__(*args, **kwargs)
        if fields:
            allowed = set(fields)
            for field_name in list(self.fields):
                if field_name not in allowed:
                    self.fields.pop(field_name)

    class Meta:
        model = UserInfo
        fields = ['website_type','user_type','extra_features','sample','color_palette','logo','text_content']
