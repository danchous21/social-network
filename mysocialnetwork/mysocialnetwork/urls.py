from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ-панель
    path('users/', include('users.urls')),  # Включение маршрутов приложения users
    path('posts/', include('posts.urls')),  # Включение маршрутов приложения posts
]
