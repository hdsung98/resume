from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from main.views import *

urlpatterns = [
  path('', index, name='index'),
  path('memo/', memo, name='memo'),
  path('memo/<int:pk>/', posting, name='posting'),
  path('memo/new_post/', new_post, name='new_post'),
  path('memo/<int:pk>/edit/', edit_post, name='edit_post'),
  path('memo/<int:pk>/delete/', delete_post, name='delete_post'),
  path('about/', about, name='about'),
  path('resume/', resume, name='resume'),
  path('services/', services, name='services'),
  path('portfolio/', portfolio, name='portfolio'),
  path('portfolio-details/', portfolio_details, name='portfolio-details'),
  path('contact/', contact, name='contact'),
  re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
  }),
  re_path(r'^static/(?:.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
