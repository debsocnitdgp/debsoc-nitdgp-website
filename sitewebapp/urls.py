from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
import django.views.defaults
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Blogs/', views.blog_home, name="blog_home"),
    path('Blogs/<int:blog_id>/', views.blog_view, name="blog_view"),
    path('Events/', views.event_home, name="event_home"),
    path('Events/<int:event_id>/', views.event_view, name="event_view"),
    path('Members/', views.members, name='members'),
    path('About/', views.about, name="about"),
    path('temp/', views.cmember, name="cmember"),
    path('accounts/', include('allauth.urls')),
    path('Audition/', views.audition, name="audition"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
