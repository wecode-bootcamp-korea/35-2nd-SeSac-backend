from django.http      import JsonResponse
from django.db.models import Q
from django.views     import View

from posts.models     import Post, Hashtag

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