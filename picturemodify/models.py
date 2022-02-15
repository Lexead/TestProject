from django.db import models
from PIL import Image


class Picture(models.Model):
    width = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.size[0] != self.width or img.size[1] != self.height:
            if self.height == None:
                img.thumbnail(
                    (self.width, self.width), Image.ANTIALIAS)
                img.save(self.image.path)
            else:
                img.resize(
                    (self.width, self.height), Image.ANTIALIAS).save(self.image.path)
