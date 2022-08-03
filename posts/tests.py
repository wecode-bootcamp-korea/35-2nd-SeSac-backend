from django.test   import TestCase, Client
from unittest.mock import patch, MagicMock

from .models       import Post, User, PostCategory, PostHashtag, Category, Hashtag, Location, Image

class PostListTest(TestCase):
    def setUp(self):
        User.objects.create(
            id                = 1,
            kakao_id          = 10,
            nickname          = '새싹',
            email             = 'a@gmail.com',
            profile_image_url = 'hi'
        )
        Location.objects.bulk_create([
            Location(
                id        = 1, 
                address   = '제주특별자치도 제주시 간월동로 32', 
                latitude  = 126.545094, 
                longitude = 33.486153),
            Location(
                id        = 2,
                address   = '강원 속초시 중앙로 46번길 45',
                latitude  = 120.43453,
                longitude = 37.028394),
            Location(
                id        = 3,
                address   = '경북 경주시 강동면 오금큰길 332-6',
                latitude  = 110.334520,
                longitude = 42.343410),
        ])
        Post.objects.bulk_create([
            Post(
                id          = 1,
                title       = '제주도에있는 카페',
                content     = 'dd',
                location_id = 1,
                user_id     = 1
            ),
            Post(
                id          = 2,
                title       = '식물가득한 수목원',
                content     = 'ㄴㄴ',
                location_id = 1,
                user_id     = 1
            ),
            Post(
                id          = 3,
                title       = '식물가득한 수목원',
                content     = 'ㅇㅈ',
                location_id = 2,
                user_id     = 1
            ),
            Post(
                id          = 4,
                title       = '식물가득한 수목원',
                content     = 'ㅇㅇ',
                location_id = 2,
                user_id     = 1
            )
        ])
        Image.objects.bulk_create([
            Image(
                id        = 1,
                image_url = 'a',
                post_id   = 1),
            Image(
                id        = 2,
                image_url = 'b',
                post_id   = 1),
            Image(
                id        = 3,
                image_url = 'c',
                post_id   = 1),
            Image(
                id        = 4,
                image_url = 'd',
                post_id   = 2),
            Image(
                id        = 5,
                image_url = 'e',
                post_id   = 2),
            Image(
                id        = 6,
                image_url = 'f',
                post_id   = 2),
            Image(
                id        = 7,
                image_url = 'g',
                post_id   = 3),
            Image(
                id        = 8,
                image_url = 'h',
                post_id   = 3),
            Image(
                id        = 9,
                image_url = 'i',
                post_id   = 3),
            Image(
                id        = 10,
                image_url = 'j',
                post_id   = 4),
            Image(
                id        = 11,
                image_url = 'k',
                post_id   = 4),
            Image(
                id        = 12,
                image_url = 'l',
                post_id   = 4)
        ])

    def tearDown(self):
        User.objects.all().delete()
        Location.objects.all().delete()
        Post.objects.all().delete()
    
    def test_success_searched_posts_list_and_random_three_posts_list(self):
        client = Client()
        response = client.get("/posts?city=제주&title_or_hashtag=식물가득")
        
        self.assertEqual(response.status_code, 200)
