from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('fun_functions.urls')),
    path('admin/', admin.site.urls),
]