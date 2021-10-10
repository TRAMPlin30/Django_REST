"""post_in URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from account.views import dashboard

# ----для URL для получения "access" и "refresh" TOKEN-ов---------
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('account/', include(('account.urls', 'account'))),
    path('api/', include(('a_p_i.urls', 'a_p_i'))),
    path('api-auth/', include(('rest_framework.urls', 'rest_framework'))), #урок 25 - (приложение не свалиться если пользователь не авторизован)

#----урок 31 ---аутентификация с помощью JWT Tokena (pip.....djangorestframework-simplejwt 4.8.0)---------------
    # ----URL для получения "access" и "refresh" TOKEN-ов---------
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
