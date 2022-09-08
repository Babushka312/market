from django.urls import path

from user.views import (
    MyObtainPairView,
    RegisterView,
    UserListApiView,
)

urlpatterns = [
    path('user/', UserListApiView.as_view(), name='user'),
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='register'),
]