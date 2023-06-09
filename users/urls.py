from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # include the default auth urls
    path('', include('django.contrib.auth.urls')),
    # include registration urls
    path('register/', views.register, name='register')
]
