from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



# urlpatterns = [
#     path('admin/', admin.site.urls),
    # path('profile/', views.profile.as_view())
# ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/', views.profile.as_view()),
    path('emp/<int:pk>/', views.profile.as_view())
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)