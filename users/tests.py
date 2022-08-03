from django.test   import TestCase, Client
from unittest.mock import patch

from users.models import User

class KakaoSocialLoginTest(TestCase):
    def setUp(self):
            pass

    def tearDown(self):
        User.objects.all().delete()

    @patch("core.utils.kakao_api.KakaoAPI.get_kakao_access_token")
    @patch("core.utils.kakao_api.KakaoAPI.get_user_kakao_information")
    def test_kakao_signin_success(self, mocked_user_info, mocked_access_token):
        client = Client()

        mocked_access_token.return_value = "access_token"
        mocked_user_info.return_value = {
            'kakao_id': 2373207523,
            'email': 'schk9611@naver.com',
            'nickname' : "위코더",
            "profile_image_url" : "http://yyy.kakao.com/.../img_110x110.jpg"
        }
        
        response = client.get('/users/login')

        self.assertEqual(response.status_code, 200)