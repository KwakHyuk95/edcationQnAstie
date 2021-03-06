"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from mathboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mathboard/', include('mathboard.urls')),
    path('krboard/', include('krboard.urls')),
    path('enboard/', include('enboard.urls')),
    path('hiboard/', include('hiboard.urls')),
    path('soboard/', include('soboard.urls')),
    path('scboard/', include('scboard.urls')),
    path('common/', include('common.urls')),
    path('', views.mainpg, name='main'),
    # path('url명', 뷰에서.가져올 함수)
    #path('', views.index),
    #path('testpage/', views.test),
    #path('<int:question_id>', views.detail)
]
