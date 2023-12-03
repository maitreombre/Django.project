from django.contrib import admin
from django.urls import path, include
from Task.views import home, signup, profile, add_friend, remove_friend, my_tasks, friend_list, accept_friend_request,\
    decline_friend_request, task_comments, add_comment, task_info, delete_comment, create_common_task, common_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Task.urls')),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', profile, name='profile'),
    path('accept_friend_request/', accept_friend_request, name='accept_friend_request'),
    path('decline_friend_request/', decline_friend_request, name='decline_friend_request'),
    path('remove_friend/', remove_friend, name='remove_friend'),
    path('profile/my_tasks/', my_tasks, name='my_tasks'),
    path('profile/friend_list/', friend_list, name='friend_list'),
    path('add_friend/', add_friend, name='add_friend'),
    path('task_comments/<int:task_id>', task_comments, name='task_comments'),
    path('add_comment/', add_comment, name='add_comment'),
    path('my_tasks/task/<int:task_id>', task_info, name='task_info'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('create_common_task/', create_common_task, name='create_common_task'),
    path('profile/common_tasks/', common_tasks, name='common_tasks'),
]
