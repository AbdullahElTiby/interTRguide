from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    # path("usearch", views.usearch, name="usearch"),
    path('<int:pk>/', views.detail, name='detail'),
    # path('voice/', views.voice_processing, name='voice_processing'),
    path('i_am_a_tourist', views.i_am_a_tourist, name='i_am_a_tourist'),
    path('<int:pk>', views.detailtor, name='detailtor'),
    # path('tr_in_blocks', views.tr_in_blocks, name='tr_in_blocks'),
    # path('chatbot', views.chatbot, name='chatbot'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('chat/', views.chat, name='chat'),
]




