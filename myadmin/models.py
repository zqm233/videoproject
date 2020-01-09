from django.db import models
from chunked_upload.models import ChunkedUpload
# Create your models here.
class MyChunkedUpload(ChunkedUpload):
    pass

MyChunkedUpload._meta.get_field('user').null = True