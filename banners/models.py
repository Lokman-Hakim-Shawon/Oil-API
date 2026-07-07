from django.db import models

# Create your models here.
class Banner(models.Model):
    image=models.URLField(blank=True,null=True)
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title