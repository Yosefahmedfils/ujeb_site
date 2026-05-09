from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, members_page, partners_page
from core import views




urlpatterns = [
    path('admin-you/', admin.site.urls),
    path('', home, name='home'),
    path('members/', members_page, name='members'),
    path('activity/<int:id>/', views.activity_detail, name='activity_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('partners/', partners_page, name='partners'),
    path('join/', views.join, name='join'),
    path('gallery/', views.gallery, name='gallery')

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)