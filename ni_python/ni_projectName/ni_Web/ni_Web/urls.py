"""ni_Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
"""
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
"""
from django.contrib import admin
from . import view,testdb,search,search2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ni_Web$', view.ni_Web),  #访问:127.0.0.1:8000\ni_Web
    url(r'^$', view.ni_Web),        #访问:127.0.0.1:8000
    url(r'^testdb$', testdb.testdb),            #访问:127.0.0.1:8000\testdb

    url(r'^search-form$', search.search_form),  #访问:127.0.0.1:8000\search-form
    url(r'^search$', search.search),            #访问:127.0.0.1:8000\search
    
    url(r'^search-post$', search2.search_post), #访问:127.0.0.1:8000\search
]

