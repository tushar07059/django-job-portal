from django.urls import path
from . import views


urlpatterns = [
    path('image',views.uplaod_image,name='upload_image'),
    path('file',views.uplaod_file,name='upload_file'),
]
