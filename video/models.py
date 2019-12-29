from django.db import models
from videoproject import settings
# Create your models here.

class Classification(models.Model):
    list_display = ("title",)
    title = models.CharField(max_length=100,blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "v_classification"


class Video(models.Model):
    STATUS_CHOICES = (
        ('0', '发布中'),
        ('1', '未发布'),
    )
    title = models.CharField(max_length=100,blank=True, null=True)
    desc = models.CharField(max_length=255,blank=True, null=True)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, null=True)
    file = models.FileField(max_length=255)
    cover = models.ImageField(upload_to='cover/',blank=True, null=True)
    status = models.CharField(max_length=1 ,choices=STATUS_CHOICES, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, max_length=20)
    view_count = models.IntegerField(default=0, blank=True)
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   blank=True, related_name="liked_videos")
    collected = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       blank=True, related_name="collected_videos")

    def switch_like(self, user):
        if user in self.liked.all():
            self.liked.remove(user)
        else:
            self.liked.add(user)

    def increase_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])


class VideoQuerySet(models.query.QuerySet):
    def get_recommend_list(self):
        return self.filter(status=0).order_by('-view_count')[:4]

