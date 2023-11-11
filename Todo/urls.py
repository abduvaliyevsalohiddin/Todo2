from django.contrib import admin
from django.urls import path

from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login_view),
    path('rejalar/', rejalar),
    path('edit/', edit),
    path('logout/', logout_view),
]
