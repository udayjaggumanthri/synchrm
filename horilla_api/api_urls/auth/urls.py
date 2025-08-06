from django.urls import path

from ...api_views.auth.views import LoginAPIView, ForgotPasswordAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view()),
    path("forgot-password/", ForgotPasswordAPIView.as_view()),
    ]
