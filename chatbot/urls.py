"""
URL configuration for chatbot project.

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

# Add this to the head of the urls.py file
from django.urls import include, path 
from django.conf.urls.static import static
from django.conf import settings


# Here we define the default endpoints for our apps
apps = [
    ('api/chat/', 'chatbot.ai_module.urls', 'ai_module'),
]

# Here we are creating path's to our apps urls
urlpatterns_apps = [path(url, include(urlconf, namespace=namespace)) for url, urlconf, namespace in apps]

# This is the default path to the admin site
urlpatterns_django = [
    path('admin/', admin.site.urls),
]

# These are the static url patterns
urlpatterns_static = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# This is the sum of all urls for the project
urlpatterns = (urlpatterns_apps + urlpatterns_django + urlpatterns_static)