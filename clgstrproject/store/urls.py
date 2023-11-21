from django.urls import path, include
from . import views
app_name='store'

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('store/', views.store, name='store'),  # new page to go after we login
    path('form/', views.form, name='form'),
    path('message/', views.message, name='message'),
]
