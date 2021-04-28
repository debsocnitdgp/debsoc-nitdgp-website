from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
import django.views.defaults
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('Audition/', views.audition, name="audition"),
    path('AuditionHome/', views.auditionhome, name="auditionhome"),
    path('AuditionForm/', views.auditionform, name="auditionform"),
    path('showdata/<email>/', views.showdata, name="showdata"),
    path('selected/', views.selectedCandidates, name="selectedList"),
    path('responses/', views.responses, name="responses"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
