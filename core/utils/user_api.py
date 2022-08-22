from django.views import View
from django.db import transaction
from django.http import JsonResponse

from users.models import User
from posts.models import Post
from comments.models import Comment

class UserAPI(View):
    def __init__(self, request):
        self.user = request.user

    def update_user_nickname(self, nickname):
        try:
            update = User.objects.get(id=self.user.id).update(nickname=nickname)

            return update

        except User.DoesNotExist:
            return JsonResponse({'message' : 'user_does_not_exist'}, status = 404)

    def delete_user_referenced_info(self):
        null_user = User.objects.get_or_create(
            kakao_id = 1234567890,
            nickname = 'null',
            email = 'null@null.com',
            profile_image_url = 'null'
        )

        with transaction.atomic():
            User.objects.get(id=self.user.id).delete()
            Post.objects.filter(user_id=self.user.id).update(user_id=null_user.id)
            Comment.objects.filter(user_id=self.user.id).update(user_id=null_user.id)

        return 'success'
