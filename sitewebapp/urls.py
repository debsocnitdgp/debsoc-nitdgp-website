from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('Blogs/', views.blog_home, name="blog_home"),
    path('Blogs/<int:blog_id>/', views.blog_view, name="blog_view"),
    path('Events/', views.event_home, name="event_home"),
    path('Events/<int:event_id>/', views.event_view, name="event_view"),
    path('Members/', views.members, name='members'),
    path('About/', views.about, name="about"),
    path('temp/', views.cmember, name="cmember"),
    path('accounts/', include('allauth.urls')),
    path('apd2/', views.apd2, name="apd2"),
    path('blogc/',views.create_blog,name="cblog"),
    path('logusr/',views.logusr,name='logusr'),
    path('adsdsd/',views.alumniadd,name='alumniadd'),
    path('Alumni/',views.view_alumni,name='alumni'),
    path('editprofile/<key>/<tok>',views.edit_profile,name="edit"),
    path('edithome/<key>',views.edit_home,name="edithome"),
    path('api/members/', views.api_member_list, name="member_api"),
    path('api/events/', views.api_event_list, name="event_api"),
    path('api/blogs/', views.api_list_blogs, name="blogs_api"),
    path('api/blog/<int:blog_id>/', views.api_get_one_blog, name="one_blog_api"),
    path('api/comments/<int:blog_id>/', views.api_get_comments, name="comments_api"),
    path('api/alumni/', views.api_get_alumni, name="alumni_api"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
