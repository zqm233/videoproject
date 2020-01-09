from django.db import models
from videoproject import settings
from video.models import Video
import datetime
# Create your models here.
class CommentQuerySet(models.query.QuerySet):

    def get_count(self):
        return self.count()

    def get_today_count(self):
        return self.exclude(timestamp__lt=datetime.date.today()).count()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30,blank=True, null=True)
    avatar = models.CharField(max_length=100,blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = CommentQuerySet.as_manager()

    class Meta:
        db_table = "v_comment"