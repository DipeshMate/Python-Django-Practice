
from django.contrib import admin
from django.urls import path, include
from drf import urls
from practice2 import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('drf.urls')),
    path('',include('drfcrud.urls')),
    path('',include('practice2.urls')),
]
