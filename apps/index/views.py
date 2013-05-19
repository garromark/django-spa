from django.contrib.auth.forms import AuthenticationForm
from apps.registration.forms import RegistrationForm
from django.template.response import TemplateResponse as TR

def index(request, template_name="index.html"):
    auth_form = AuthenticationForm()
    # these are not in the AuthenticationForm by default
    auth_form.fields["username"].widget.attrs["placeholder"] = "Username"
    auth_form.fields["password"].widget.attrs["placeholder"] = "Password"
    return TR(request,
              template_name,
              {'login_form': auth_form,
               'registration_form': RegistrationForm()})
