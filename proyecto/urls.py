from django.contrib import admin
from django.urls import path
from app1 import views as app1_views
from app2 import views as app2_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/vista1/', app1_views.vista1),
    path('app1/vista2/', app1_views.vista2),
    path('app2/vista1/', app2_views.vista1),
    path('app2/vista2/', app2_views.vista2),
]
