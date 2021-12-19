from django.urls import path, re_path, include
from comment.views import CommentView

app_name = 'comment'
urlpatterns = [
    path('comment/', CommentView.as_view(), name='show_comment'),
]
