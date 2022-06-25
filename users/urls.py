from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, LoginView, UserView, LogOutView, AddLinkView, GetLinksView, UpdateLinksView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('user', UserView.as_view(), name='user'),
    path('logout', LogOutView.as_view(), name='logout'),
    path('link', AddLinkView.as_view(), name='link'),
    path('getlinks', GetLinksView.as_view(), name='get-links'),
    path('updatelinks', UpdateLinksView.as_view(), name='update-links')
]
