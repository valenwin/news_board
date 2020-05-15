from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User,
                               related_name='posts',
                               on_delete=models.CASCADE)
    link = models.URLField(max_length=1000)
    upvotes = models.ManyToManyField(User, related_name="like_voters")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.author}: {self.link}'


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.author.first_name} leave comment on {self.post.title}'
