import boto3

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from users.utils        import login_decorator
from .models            import Post, PostCategory, Category, PostHashtag, Hashtag, Location, Image, Hashtag
from posts.models       import Post, Hashtag
from core.util         import ImageHandler, ImageUploader
from fresh_us.settings  import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID
from users.models       import User

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

    @login_decorator
    def delete(self, request, post_id):
        try:
            if request.user == None:
                return JsonResponse({'message' : 'UNAUTHORIZED_USER'}, status=403)
            
            user_id   = User.objects.get(id=request.user.id).id 
            
            if Post.objects.get(id=post_id).user.id == user_id:
                Location.objects.get(post__id=post_id).delete()
                
                for image in Image.objects.filter(post_id=post_id):
                    image_name    = image.image_url.split('/')[-1]
                    image_handler = ImageHandler(image_uploader, image_name)
                    image_handler.delete()
                Image.objects.filter(post_id=post_id).delete()
                
                Post.objects.get(id=post_id).delete()
                PostCategory.objects.filter(post_id=post_id).delete()
                PostHashtag.objects.filter(post_id=post_id).delete()
                
                return JsonResponse({"message": "DELETE_SUCCESS"}, status=204)
            
            return JsonResponse({"message": "USER_DOES_NOT_WROTE_THIS_POST"}, status=403)
        
        except Post.DoesNotExist:
            return JsonResponse({'message': 'POST_DOES_NOT_EXIST'}, status=400)
    
    def get(self, request, post_id):
        try:
            if request.user == None:
                user_id = "NOT_LOG_IN_USER"
            else:
                user_id = User.objects.get(id=request.user.id).id
            
            post = Post.objects.select_related('user', 'location')\
                .prefetch_related('category')\
                .get(id=post_id)

            result  = {
                "user_id"                       : user_id,
                "post_id"                       : post_id,
                "written_user_id"               : post.user.id,
                "written_user_name"             : post.user.nickname,
                "written_user_profile_image_url": post.user.profile_image_url,
                'created_at'                    : post.created_at,
                "address"                       : post.location.address,
                "latitude"                      : post.location.latitude,
                "longitude"                     : post.location.longitude,
                "title"                         : post.title,
                "images"                        : [{
                    "id"  : image.id,
                    "url" : image.image_url
                    }for image in Image.objects.filter(post_id=post_id)],
                "content"          : post.content,
                "hashtags"         : [{
                    "id" : hashtag.id,
                    "name" : hashtag.name
                    }for hashtag in Hashtag.objects.filter(posthashtag__post_id=post_id)]
            }
            return JsonResponse({"result": result}, status=200)

        except Post.DoesNotExist:
            return JsonResponse({'message': 'POST_DOES_NOT_EXIST'}, status=400)

class PostListView(View):
    def get(self, request):
        city             = request.GET.get('city')
        town             = request.GET.get('town')
        title_or_hashtag = request.GET.get('title_or_hashtag')
        categories       = request.GET.get('categories')
        offset           = int(request.GET.get('offset', 0))
        
        q = Q()

        if categories:
            categories = categories.split(',')
            for category in categories:
                q |= Q(category__name = category)
        if city:
            q &= Q(location__address__icontains = city)
        if town:
            q &= Q(location__address__icontains = town)
        if title_or_hashtag:
            q &= (Q(title__icontains = title_or_hashtag) | Q(posthashtag__hashtag__name__icontains = title_or_hashtag))

        posts      = Post.objects.filter(q).distinct()
        posts_list = posts[offset:offset+8]
        
        result = [
            {
                'id'      : post.id,
                'title'   : post.title,
                'address' : post.location.address,
                'hashtags': [
                    {
                        "id"  : hashtag.id,
                        "name": hashtag.name
                    } for hashtag in Hashtag.objects.filter(posthashtag__post__id = post.id)],
                'images'  : [
                    {
                        "id": image.id,
                        "url": image.image_url
                    } for image in post.image_set.all()]
            }for post in posts_list
        ]

        recommended_posts     = Post.objects.all().order_by('?')[:3]
        recommended_post_list = [
            {
                'id'       : post.id,
                'title'    : post.title,
                'latitude' : post.location.latitude,
                'longitude': post.location.longitude,
                'hashtags' : [
                    {
                        "id"  : hashtag.id,
                        "name": hashtag.name
                    } for hashtag in Hashtag.objects.filter(posthashtag__post__id = post.id)],
                'image'   : {
                    "id"  : post.image_set.first().id,
                    "url" : post.image_set.first().image_url
                    }
            }for post in recommended_posts
        ]

        return JsonResponse(
            {
                'result'               : result,
                'total_posts'          : posts.count(),
                'recommended_post_list': recommended_post_list
            }, status=200)
