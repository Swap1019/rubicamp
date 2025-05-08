from django.shortcuts import redirect

class UserWebsiteOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_ownwebsite:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('rubikamp:user-website-create')  # use a named URL here
