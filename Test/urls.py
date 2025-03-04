from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Définition du schéma de l'API
schema_view = get_schema_view(
    openapi.Info(
        title="Gestion Comptable API",
        default_version='v1',
        description="API pour la gestion comptable",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger et Redoc pour afficher la documentation de l'API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Autres URLs de votre application
    path('', include('accounting.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),

    # Endpoints pour l'authentification JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
