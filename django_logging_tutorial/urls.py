from django.contrib import admin
from django.urls import path
from logging_example import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello_reader, name="hello_reader")
]
