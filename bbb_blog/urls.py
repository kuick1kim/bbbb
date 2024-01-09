from django.urls import path
from bbb_blog import views


urlpatterns = [
    path("", views.index, name="index"),
    # path("index/", views.index, name="index2"),
    path("fashion/", views.fashion, name="fashion"),
    path("about/", views.about_1, name="about"),
    path("photography/", views.photo1, name="photography"),
    path("travel/", views.travel1, name="travel"),
    path("contact/", views.contact1, name="contact"),
    path("single/", views.single1, name="single"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
    path("post/create", views.PostCreate.as_view(), name="post_create"),
    path('remove_post/<int:post_id>/', views.RemovePostView.as_view(), name='remove_post'),
    
    # path("a/", views.fashion, name="fashion")
]