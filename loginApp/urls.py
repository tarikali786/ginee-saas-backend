from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from .views import RegisterAPI,login_cred,LogoutView

from .views import GoogleSocialAuthView, FacebookSocialAuthView, VerifyEmail, ResendEmailVerification,SSOAuthView

urlpatterns = [
    path('register/', RegisterAPI, name='register_user'),
    path('login/', login_cred, name='user_login_with_cred'),
    path('logout/',LogoutView.as_view(), name='logout_user'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('email-verify/resend/', ResendEmailVerification.as_view(), name="email-verify-resend"),
    path('google/', GoogleSocialAuthView.as_view()),
    path('facebook/', FacebookSocialAuthView.as_view()),
    path('sso/', SSOAuthView.as_view()), 
    
]