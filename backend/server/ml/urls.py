from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *
  
urlpatterns = [ 
    path('image_upload', image_upload_view, name = 'image_upload'), 
    path('images_list', ImageList.as_view(), name = 'image_list'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image_detail'), 
] 
  
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT) 