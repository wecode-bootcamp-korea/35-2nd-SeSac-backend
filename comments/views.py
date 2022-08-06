import json

from django.views import View
from django.http  import JsonResponse

from users.models               import User
from comments.models            import Comment
from posts.models               import Post
from core.utils.login_decorator import login_decorator

class CommentView(View):
    @login_decorator
    def get(self, request, post_id):
        user   = request.user
        limit  = int(request.GET.get('limit', 5))
        offset = int(request.GET.get('offset', 0))

        comments_total = Comment.objects.all().count()
        comments       = Comment.objects.filter(post=post_id, parent_comment_id=0).order_by('-created_at')

        user_id = None
        if not user == None:    
            user_id = user.id

        result = []

        for comment in comments:
            result.append({
                'id'               : comment.id,
                'user_id'          : comment.user_id,
                'parent_comment_id': comment.parent_comment_id,
                'profile_image_url': comment.user.profile_image_url,
                'nickname'         : comment.user.nickname,
                'comment'          : comment.comment,
                'created_at'       : comment.created_at,
                'depth'            : 0
            })
            for review in Comment.objects.filter(parent_comment_id=comment.id).order_by('-created_at'):
                result.append({
                    'id'               : review.id,
                    'user_id'          : review.user_id,
                    'parent_comment_id': review.parent_comment_id,
                    'profile_image_url': review.user.profile_image_url,
                    'nickname'         : review.user.nickname,
                    'comment'          : review.comment,
                    'created_at'       : review.created_at,
                    'depth'            : 1
                })

        result_res = {'comment' : result[offset : offset + limit]}

        result_res['user_id']        = user_id
        result_res['comments_total'] = comments_total

        return JsonResponse(result_res, status = 200, safe=False)

    @login_decorator
    def post(self, request, post_id):
        try:
            data              = json.loads(request.body)
            user              = request.user
            parent_comment_id = data['parent_comment_id']
            comment           = data['comment']

            if user == None:
                return JsonResponse({'message' : 'UNAUTHORIZED_USER'}, status = 403)

            if not parent_comment_id == 0:
                if not Comment.objects.filter(id=parent_comment_id).exists():
                    return JsonResponse({'message' : 'PARENT_COMMENT_NOT_EXIST'}, status = 404)

            Comment.objects.create(
                post              = Post.objects.get(id=post_id),
                user              = User.objects.get(id=user.id),
                parent_comment_id = parent_comment_id,
                comment           = comment,
            )

            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

    @login_decorator
    def patch(self, request, post_id, comment_id):
        try:
            data    = json.loads(request.body)
            user    = request.user
            comment = data['comment']

            if user == None:
                return JsonResponse({'message' : 'UNAUTHORIZED_USER'}, status = 403)

            if not Comment.objects.filter(post=post_id, id=comment_id).exists():
                raise Exception({'message' : 'DATA_INVAILD'})

            if not Comment.objects.filter(id=comment_id, user=user).exists():
                raise Exception({'message' : 'NOT_A_USER_COMMENT'})

            Comment.objects.filter(id=comment_id).update(comment=comment)

            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

    @login_decorator
    def delete(self, request, post_id, comment_id):
        try:
            user = request.user

            if user == None:
                return JsonResponse({'message' : 'UNAUTHORIZED_USER'}, status = 403)

            if not Comment.objects.filter(post=post_id, id=comment_id).exists():
                raise Exception({'message' : 'DATA_INVAILD'}, status = 400)
    
            if not Comment.objects.filter(id=comment_id, user=user).exists():
                raise Exception({'message' : 'NOT_A_USER_COMMENT'})

            Comment.objects.filter(parent_comment_id = comment_id).delete()
            Comment.objects.filter(id=comment_id, user=user).delete()
            
            return JsonResponse({'message' : 'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)