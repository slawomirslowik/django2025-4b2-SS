from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path('admin/', admin.site.urls),
    path('polls/', include("polls.urls"))
]
