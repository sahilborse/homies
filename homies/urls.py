"""
URL configuration for homies project.

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
from django.contrib import admin
from django.urls import path,include

#changes to be made in admin site text
admin.site.site_header = "Vasu first"
admin.site.site_title = "Vasu club Portal"
admin.site.index_title = "Welcome to Vasu Researcher Portal"

# different path of urls are gven from here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('work.urls'))
]
