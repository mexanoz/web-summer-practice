from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from info import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(), name = "login"),
    path("logout/", auth_views.LogoutView.as_view(), name = "logout"),
    path("info/", include("info.urls")),
    path("", views.redirect_view),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
