# schoolwebsite/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ──────────────── Admin & API Routes ────────────────
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),  # ✅ API base prefix

    # ──────────────── React Frontend (Catch-all) ────────────────
    # Serves your React app for any unknown route
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html")),
]

# ──────────────── Media Serving (✅ For user uploads) ────────────────
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
