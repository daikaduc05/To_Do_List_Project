"""
URL configuration for To_Do_List project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from . import views
urlpatterns = [
   path('signup/',views.signup,name ='signup'),
   path('login/',views.user_login,name = 'login' ),
   path('home/',views.home,name = 'home'),
   path('logout/',views.user_logout,name = 'logout'),
   path('form/<int:this_task_id>/<str:type>',views.form,name = 'form'),
   path('delete/<int:id_need_delete>',views.delete,name = 'delete'),
   path('error/',views.error,name = 'error')
]
