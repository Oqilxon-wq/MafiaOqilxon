from django.urls import path
from .views import *

urlpatterns = [
    path('v1/login/', Login_API.as_view(), name='Bu login page uchun yozilgan kod'),
    path('v1/verify/', VerifyAccount.as_view()),
    path('v1/register/', RegisterMafiaUser.as_view()),
    path('v1/checkemailcode/', VerifyLogin.as_view()),
    path('v1/create/lobby', CreateRoom.as_view()),
    path('v1/join/lobby', JoinRoom.as_view()),
    path('v1/start/game/',StartGame.as_view()),
    path('v1/game/<pk>/', GameInformationView.as_view()),
    path('v1/setdead/', SetDeadView.as_view())


    # path('v1/get/', MafiaUserCreateView.as_view()),
    # path('v1/verification/', OTPVerificationView.as_view()),
]
