"""
URL configuration for ODP project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from home import views as v1
from signup import views as v2
from login import views as v3
from aboutus import views as v4
from contactus import views as v5
from dashboard import views as v6 





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.home,name='home'),#set as landing page ar home page
    path('signup/',v2.signup,name="signup"),
    path('login/',v3.login,name="login"),
    path('aboutus/',v4.aboutus,name="aboutus"),
    path('contactus',v5.contactus,name='contactus'),
    path('dashboard/',v6.dashboard,name='dashboard'),
    path('studentapp/', include('studentapp.urls')),
    path('logout/', v2.logout_view, name='logout'),  
    

]

