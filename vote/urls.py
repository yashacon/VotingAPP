from django.urls import path

from . import views

urlpatterns=[
    path('',views.login,name='Login'),
    path('register',views.register,name='Register'),
    path('logout',views.logout,name='Logout'),
    path('vote',views.vote,name='Vote'),
    path('<str:title>/',views.voting,name='Voting'),
    path('add',views.AddItem,name='AddItem')
]
