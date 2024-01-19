"""
URL configuration for hub_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from redirector.views import home, redirect_app1, redirect_app2, redirect_app3, redirect_chatbot_frontend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('app1/', redirect_app1),
    path('app2/', redirect_app2),
    path('app3/', redirect_app3),
    path('genai/home', redirect_chatbot_frontend),
]
