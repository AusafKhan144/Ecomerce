from django.urls import path
from authenticate.views import *

urlpatterns = [
    path('', SigninView.as_view(), name='signin'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signout/', SignoutView.as_view(), name='signout'),
]