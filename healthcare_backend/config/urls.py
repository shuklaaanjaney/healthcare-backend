from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patients.views import PatientViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from doctors.views import DoctorViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'doctors', DoctorViewSet, basename='doctors')

urlpatterns = [
    path('admin/', admin.site.urls),

    
    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
    path('api/', include(router.urls)),
    path("api/mappings/", include("mappings.urls")),
]

