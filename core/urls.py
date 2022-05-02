from django.urls import path

from .views import (
    home,
    user_posts,
    about,
    contact,
    post_detail,
    create_view,
    delete_view,
    update_view,
)


urlpatterns = [
    #template
    path('', home, name='home'),
    path('posts/<str:username>/', user_posts, name='userposts'),
    #detail
    path('post/<int:pk>/', post_detail, name='detail'),
    #CRUD
    path('post/new/', create_view, name='create'),
    path('post/<int:pk>/delete/', delete_view, name='delete'),
    path('post/<int:pk>/update/', update_view, name='update'),
    #template
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    #search
]