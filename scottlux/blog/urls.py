from django.urls import include,path
from django.contrib.auth import views as auth_views

from . import views

auth_views.LogoutView.next_page = '/blog/login'

urlpatterns = [
	path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view()),
    path('loggedin/', views.logged),
    path('create/', views.tocreate),
    path('created/',views.create, name = 'create'),
    path('show/', views.show),
    path('post/<int:post_id>/', views.view),
]