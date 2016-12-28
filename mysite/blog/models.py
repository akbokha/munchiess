from django.db import models
from django.utils import timezone
from stdimage import StdImageField

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = StdImageField(blank=False, default="", variations={'resize': (420, 160, True)}) 
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    category = models.CharField(
        max_length=9,
        choices= (
        ('breakfast', 'Breakfast'),
        ('dinner', 'Dinner'),
        ('snacks', 'Snacks'),
        ),
        default='snacks',
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
