from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from member.models import Member

# BoardModel
class Board(models.Model):
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254, default='list') # list/gallery

    def __str__(self):
        return self.name

# PostModel
class Post(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    content = models.TextField()
    writer = models.ForeignKey(Member, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# CommentModel
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(Member, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.content