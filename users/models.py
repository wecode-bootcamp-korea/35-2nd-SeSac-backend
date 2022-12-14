from django.db   import models

from core.models import TimeStampModel

class User(TimeStampModel):
    kakao_id          = models.BigIntegerField()
    nickname          = models.CharField(max_length=20)
    email             = models.CharField(max_length=50)
    profile_image_url = models.CharField(max_length=150, null=True)

    class Meta:
        db_table = 'users'
