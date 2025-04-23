import logging

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.db import transaction
from django.shortcuts import render, redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views import generic, View

from accounts.forms import CustomUserCreationForm
from accounts.services.token_service import account_activation_token
from accounts.services.user_service import UserService


class SignUpGenericView(generic.CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    @transaction.atomic
    def form_valid(self, form):
        try:
            site_url = get_current_site(self.request)
            domain = site_url.domain
            password = form.cleaned_data["password1"]

            UserService.create_user(
                **form.cleaned_data, password=password, domain=domain
            )
        except Exception as e:
            logging.error(f"Error sending email: {e}")

            return render(self.request, "registration/signup.html", {"form": form})

        return render(self.request, "registration/email_confirmation_sent.html")


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            # login(request, user)
            messages.success(
                request,
                "Thank you for confirming your email. You can now login to your account.",
            )
            return redirect("accounts:login")
        else:
            return render(request, "registration/activation_invalid.html")
