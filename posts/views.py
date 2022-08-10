import boto3

from urllib.parse import unquote
from django.http  import JsonResponse
from django.views import View

from my_settings  import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID
from users.utils  import login_decorator
from .models      import Post, PostCategory, Category, PostHashtag, Hashtag, Location, Image
from core.utils   import ImageHandler, ImageUploader

s3_client = boto3.client(
        's3',
        aws_access_key_id     = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

image_uploader = ImageUploader(s3_client)

class PostView(View):
    @login_decorator
    def post(self, request):
        try:
            if request.user == None:
                return JsonResponse({'message' : 'UNAUTHORIZED_USER'}, status=403)

            data       = request.POST
            categories = data['categories'].split(',')[:-1]
            hashtags   = data['hashtags'].split(',')[:-1]
            files      = request.FILES.getlist('image')

            location = Location.objects.create(
                address   = data['address'],
                latitude  = data['latitude'],
                longitude = data['longitude']
            )

            post = Post.objects.create(
                user_id     = request.user.id,
                location_id = location.id,
                title       = data['title'],
                content     = data['content']
            )

            for file in files:
                image_handler = ImageHandler(image_uploader, file)
                url = image_handler.save()
                Image.objects.create(
                    post_id = post.id,
                    image_url = url
                )

            for category in categories:
                PostCategory.objects.get_or_create(
                    post_id     = post.id,
                    category_id = Category.objects.get(name=category).id
                )

            for hashtag in hashtags:
                hashtag, created = Hashtag.objects.get_or_create(
                    name = hashtag
                )
                PostHashtag.objects.get_or_create(
                    post_id     = post.id,
                    hashtag_id = hashtag.id
                )
            return JsonResponse({"message": "CREATED"}, status=201)

        except Category.DoesNotExist:
            return JsonResponse({'message': 'CATEGORY_DOES_NOT_EXIST'}, status=400)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

