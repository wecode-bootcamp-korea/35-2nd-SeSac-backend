from django.db    import models

from core.models  import TimeStampModel
from users.models import User
from posts.models import Post

class Comment(TimeStampModel):
    post              = models.ForeignKey(Post, on_delete=models.CASCADE)
    user              = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment_id = models.IntegerField()
    comment           = models.TextField()

    class Meta:
        db_table = 'comments'