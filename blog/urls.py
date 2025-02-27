from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'  

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_list, name='blog_list'),
    path('create-post/', views.create_post, name='create_post'),
    path('<int:blog_post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
    path('accounts/profile/', views.profile, name='profile'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:post_id>/like/', views.like_post, name='like_post'),
    path('signup/', views.signup_view, name='signup'),
    path('create/', views.create_post, name='create_blog'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    


