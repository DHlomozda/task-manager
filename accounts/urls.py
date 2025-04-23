from django.urls import path, include

from accounts.views import ActivateAccountView, SignUpGenericView

app_name = "accounts"

urlpatterns = [
    path("signup/", SignUpGenericView.as_view(), name="signup"),
    path("activate/<uidb64>/<token>/", ActivateAccountView.as_view(), name="activate"),
    path("", include("django.contrib.auth.urls")),
]