import json
import jwt

from django.test import Client, TestCase
from django.conf import settings

from users.models    import User
from comments.models import Comment
from posts.models    import Location, Post

class CommentGetTest(TestCase):

    maxDiff = None

    def setUp(self):
        self.client       = Client()
        self.access_token = jwt.encode({'user_id' : 1}, settings.SECRET_KEY, settings.ALGORITHM)

        Location.objects.create(
            id = 1,
            address = "서울특별시 구로구 항동 96-4",
            latitude = 123.456789,
            longitude = 123.456789
        )
        User.objects.bulk_create(
            User(
                id = 1,
                kakao_id = 100001,
                nickname = '김코더',
                email = "test@test.com",
                profile_image_url = "http://yyy.kakao.com/.../img_110x110.jpg"
            ),
            User(
                id = 2,
                kakao_id = 100002,
                nickname = '이코더',
                email = "test@test.com",
                profile_image_url = "http://yyy.kakao.com/.../img_110x110.jpg"
            ),
            User(
                id = 3,
                kakao_id = 100003,
                nickname = '손코더',
                email = "test@test.com",
                profile_image_url = "http://yyy.kakao.com/.../img_110x110.jpg"
            ),
            User(
                id = 4,
                kakao_id = 100004,
                nickname = '박코더',
                email = "test@test.com",
                profile_image_url = "http://yyy.kakao.com/.../img_110x110.jpg"
            )
        )
        Post.objects.create(
            id = 1,
            title = "이쁜 수목원",
            content = "이뻐요~",
            location = Location.objects.get(id=1),
            user = User.objects.get(id=1)
        )
        Comment.objects.bulk_create(
            Comment(
                id = 1,
                post = Post.objects.get(id=1),
                user = User.objects.get(id=1),
                parent_comment_id = 0,
                comment = "장소가 너무 이쁘네요~", 
            ),
            Comment(
                id = 2,
                post = Post.objects.get(id=1),
                user = User.objects.get(id=2),
                parent_comment_id = 0,
                comment = "다음에 꼭 가보고 싶어요!",
            ),
            Comment(
                id = 3,
                post = Post.objects.get(id=1),
                user = User.objects.get(id=3),
                parent_comment_id = 1,
                comment = "공감합니다",
            ),
            Comment(
                id = 4,
                post = Post.objects.get(id=1),
                user = User.objects.get(id=3),
                parent_comment_id = 0,
                comment = "저번에 가봤던 곳인데 너무 좋아요!!",
            ),
            Comment(
                id = 5,
                post = Post.objects.get(id=1),
                user = User.objects.get(id=4),
                parent_comment_id = 3,
                comment = "Me too",
            )
        )

    def tearDown(self):
        Location.objects.all().delete()
        Comment.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()

    # def test_success_get_comments(self):
    #     self.client       = Client()
    #     self.access_token = jwt.encode({'user_id' : 1}, settings.SECRET_KEY, settings.ALGORITHM)
    #     headers      = {'HTTP_AUTHORIZATION' : self.access_token}
    #     response     = self.client.get("/posts/1/comments?limit=5&offset=0", **headers)
    #     print(Comment.objects.get(id=1).created_at)
    #     self.assertEqual(response.json(),
    #         {
    #             'user_id' : 1,
    #             'comment' : [
    #                 {
    #                     'id' : 1,
    #                     'user_id' : 1,
    #                     'parent_comment_id' : 0,
    #                     'profile_image_url' : "http://yyy.kakao.com/.../img_110x110.jpg",
    #                     'nickname' : '김코더',
    #                     'comment' : "장소가 너무 이쁘네요~",
    #                     'created_at' : Comment.objects.get(id=1).created_at,
    #                 },
    #                 {
    #                     'id' : 2,
    #                     'user_id' : 2,
    #                     'parent_comment_id' : 0,
    #                     'profile_image_url' : "http://yyy.kakao.com/.../img_110x110.jpg",
    #                     'nickname' : '이코더',
    #                     'comment' : "다음에 꼭 가보고 싶어요!",
    #                     'created_at' : Comment.objects.get(id=2).created_at,
    #                 },
    #                 {
    #                     'id' : 3,
    #                     'user_id' : 3,
    #                     'parent_comment_id' : 1,
    #                     'profile_image_url' : "http://yyy.kakao.com/.../img_110x110.jpg",
    #                     'nickname' : '손코더',
    #                     'comment' : "공감합니다",
    #                     'created_at' : Comment.objects.get(id=3).created_at,
    #                 },
    #                 {
    #                     'id' : 4,
    #                     'user_id' : 3,
    #                     'parent_comment_id' : 0,
    #                     'profile_image_url' : "http://yyy.kakao.com/.../img_110x110.jpg",
    #                     'nickname' : '손코더',
    #                     'comment' : "저번에 가봤던 곳인데 너무 좋아요!!",
    #                     'created_at' : Comment.objects.get(id=4).created_at,
    #                 },
    #                 {
    #                     'id' : 5,
    #                     'user_id' : 4,
    #                     'parent_comment_id' : 3,
    #                     'profile_image_url' : "http://yyy.kakao.com/.../img_110x110.jpg",
    #                     'nickname' : '박코더',
    #                     'comment' : "Me too",
    #                     'created_at' : Comment.objects.get(id=5).created_at,
    #                 }
    #             ]
    #         }
    #     )
    #     self.assertEqual(response.status_code, 200)

    def test_success_post_comment(self):
        headers      = {'HTTP_AUTHORIZATION' : self.access_token}
        data         = {'parent_comment_id' : 0, 'comment' : "아주 좋습니다"}
        response     = self.client.post("/posts/1/comments", json.dumps(data), content_type="application/json", **headers)

        self.assertEqual(response.status_code, 201)

    def test_success_post_comment(self):
        headers      = {'HTTP_AUTHORIZATION' : self.access_token}
        data         = {'parent_comment_id' : 0, 'comment' : "아주 좋습니다"}
        response     = self.client.post("/posts/1/comments", json.dumps(data), content_type="application/json", **headers)

        self.assertEqual(response.status_code, 201)

    def test_exception_post_comment_parent_comment_not_exist(self):
        headers      = {'HTTP_AUTHORIZATION' : self.access_token}
        data         = {'parent_comment_id' : 9, 'comment' : "아주 좋습니다"}
        response     = self.client.post("/posts/1/comments", json.dumps(data), content_type="application/json", **headers)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json(), {'message' : 'PARENT_COMMENT_NOT_EXIST'})

    def test_success_post_comment_key_error(self):
        headers      = {'HTTP_AUTHORIZATION' : self.access_token}
        data         = {'parent_comment_id' : 0}
        response     = self.client.post("/posts/1/comments", json.dumps(data), content_type="application/json", **headers)

        self.assertEqual(response.status_code, 400)

    def test_success_patch_comment(self):
        headers      = {'HTTP_AUTHORIZATION' : self.access_token}
        data         = {'comment' : "수정 했어요."}
        response     = self.client.patch("/posts/1/comments/1", json.dumps(data), content_type="application/json", **headers)

        self.assertEqual(response.status_code, 201)

    def test_success_delete_comment(self):
        headers      = {'HTTP_AUTHORIZATION' : self.access_token}
        response     = self.client.delete("/posts/1/comments/1", **headers)

        self.assertEqual(response.status_code, 200)
