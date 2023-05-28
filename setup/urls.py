from django.urls.conf import path
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url = 'register/')),
    path('register/',register,name = 'register_page'),
    path('home/',home,name = 'home'),
    path('logout/',logout,name = 'logout_user'),
    path('quize_start/',startquize,name = 'quize_start'),
    path('checkAns/<int:pk>/<str:ans>/<str:user>/',checkAns,name = 'check__Ans'),
    path('all_done/',alldone,name = 'all_done'),
    
    
    
]