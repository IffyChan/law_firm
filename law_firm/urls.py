from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),          # Главная страница
    path('clients/', include('clients.urls')),  # Управление клиентами
    path('feedback/', include('feedback.urls')), # Обратная связь
    path('blog/', include('blog.urls')),        # Блог
   # path('court_timer/', include('court_timer.urls')), # Таймер
]
