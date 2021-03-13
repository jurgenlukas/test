from django.contrib import admin
from django.urls import path,include
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    # path函数将url映射到视图
    path('', views.article_list, name='article_list'),
    path('<int:id>/', views.article_detail, name='article_detail'),
    path('create/', views.article_create, name='createe'),
    path('delete/<int:id>/', views.delete, name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

