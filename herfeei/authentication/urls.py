from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from herfeei.authentication.apis.auth import (LoginByUsernameView,
                                              VerifyAuthenticationView)

urlpatterns = [
    path("", LoginByUsernameView.as_view(), name="login-by-username"),
    path("verify/", VerifyAuthenticationView.as_view(), name="verify"),
    path('jwt/',
         include([
             path('refresh/', TokenRefreshView.as_view(), name="refresh"),
             path('verify/', TokenVerifyView.as_view(), name="verify"),
         ]),
         name="jwt"),
]
