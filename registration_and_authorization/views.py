from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseRedirect
from . import forms, models
from django.urls import reverse


class RegistrationView(generic.CreateView):
    template_name = 'registration_and_authorization/registration.html'
    form_class = forms.CustomRegistrationForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        self.send_verification_email(user, self.request)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('users:email_verification_sent')

    def send_verification_email(self, user, request):
        current_site = get_current_site(request)
        subject = 'Confirm your email'
        message = render_to_string('registration_and_authorization/email_confirmation.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        send_mail(subject, message, 'from@example.com', [user.email])


class EmailVerificationSentView(generic.TemplateView):
    template_name = 'registration_and_authorization/email_verification_sent.html'


class AuthorizationView(LoginView):
    template_name = 'registration_and_authorization/authorization.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse("users:greeting")


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class GreetingView(generic.ListView):
    template_name = 'registration_and_authorization/greeting.html'
    context_object_name = 'greet'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()
