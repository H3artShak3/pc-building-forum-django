from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forum/', views.get_postai, name='forum-main'),
    path('forum/threads/<str:cat>', views.get_postai_by_cat, name='forum'),
    path('pc-calculator/', views.get_all_setup_parts, name='bootleneck-calc'),
    path('forum/thread/<int:pk>', views.ThreadDetailView.as_view(), name='thread-one'),
    path('profilis/', views.profilis, name='profilis-url'),
    path('register/', views.register_user, name='register-url'),
    path('myposts/', views.UserPostaiListView.as_view(), name='my-postai'),
    path('myposts/new', views.PostasByUserCreateView.as_view(), name='my-postas-new'),
    path('myposts/update/<int:pk>', views.PostasByUserUpdateView.as_view(), name='my-postas-update'),
    path('advertisements/', views.get_advertisements, name='adverts'),
    path('advertisements/pc', views.get_advertisements_pc, name='adverts-pc'),
    path('advertisements/cpu', views.get_advertisements_cpu, name='adverts-cpu'),
    path('advertisements/gpu', views.get_advertisements_gpu, name='adverts-gpu'),
    path('advertisements/ram', views.get_advertisements_ram, name='adverts-ram'),
    path('myads/new', views.AdvertisementByUserCreateView.as_view(), name='my-ad-new'),
    path('advertisements/ext/<int:pk>', views.AdvertisementDetailView.as_view(), name='ad-one'),
]