from django.urls import path
from .views import AssignDoctorToPatientView

urlpatterns = [
    path("assign/", AssignDoctorToPatientView.as_view(), name="assign-doctor"),
]
