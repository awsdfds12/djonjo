from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")

_____________________________________________________________________________________________________

from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]

_______________________________________________________________________________________________________

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello_world_app.urls')),  # Include the app's URLs
]

