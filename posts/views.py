import boto3

from django.http  import JsonResponse
from django.views import View

from fresh_us.settings  import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID
from users.utils        import login_decorator
from .models            import Post, Image, Hashtag, Category
from users.models       import User
from decorators         import query_debugger

class PostDetailView(View):
    '''
    1. id 값 같이 반환
    2. orm 최적화
    '''
    @query_debugger
    # @login_decorator
    def get(self, request, post_id):
        try:
            # if request.user == None:
            #     return JsonResponse({'message' : 'UNAUTHORIZED_USER'}, status=403)
            
            # user_id = User.objects.get(id=request.user.id).id
            post    = Post.objects.select_related('user', 'location')\
                                  .prefetch_related('category')\
                                  .get(id=post_id)

                                #   .get(id=post_id)
            
            result  = {
                "user_id"          : 1,
                "post_id"          : post_id,
                "categories"       : [{
                    'id'   : category.id,
                    'name' : category.name 
                    # } for category in Category.objects.filter(postcategory__post_id=post_id)],
                    } for category in post.category.all()],
                "written_user_id"  : post.user.id,
                "written_user_name": post.user.nickname,
                "location"         : post.location.address,
                "latitude"         : post.location.latitude,
                "longitude"        : post.location.longitude,
                "title"            : post.title,
                "images"           : [image.image_url for image in Image.objects.filter(post_id=post_id)],
                "content"          : post.content,
                "hashtags"         : [hashtag.name for hashtag in Hashtag.objects.filter(posthashtag__post_id=post_id)]
            }
            return JsonResponse({"result": result}, status=200)

        except Post.DoesNotExist:
            return JsonResponse({'message': 'POST_DOES_NOT_EXIST'}, status=400)