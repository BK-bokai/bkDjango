from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail

# Create your models here.
class Images(models.Model):
    path    = models.TextField()
    # path    = models.ImageField()
    publish = models.BooleanField()
    index   = models.BooleanField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField(null=True) 
    # def save(self, *args, **kwargs):
    #     if self.path:
    #         self.path = get_thumbnail(self.path, '500x500', quality=99, format='JPEG')
    #     super().save(*args, **kwargs)