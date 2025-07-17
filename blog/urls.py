from django.urls import path
from .apis import *

urlpatterns = [
    path('user/register/', UserRegisterAPI.as_view()), # User Register API
    path('user/login/', UserLoginAPI.as_view()), # User Login API
    path('post_blog/', PostBlogAPI.as_view()), # Post Blog API
    path('edit_blog/<int:id>/', EditBlogAPI.as_view()), # Edit Blog API
    path('delete_blog/<int:id>/', DeleteBlogAPI.as_view()), # Delete Blog API
    path('blog_list/', GetBlogListAPI.as_view()), # Get Blog List API
]
