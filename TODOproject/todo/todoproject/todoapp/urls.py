from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [

    path('',views.add,name='add'),
    # path('index/',views.index,name='index')
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvadd/',views.Tasklistview.as_view(),name='cbvadd'),
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)