from django.db import models

class Author(models.Model):
    name = models.CharField(
        verbose_name= 'Author Name',
        max_length=50,
        null=False,
        blank=False
    )
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']

class Tag(models.Model):
    name = models.CharField(
        verbose_name= 'Tag Name',
        max_length=50,
        null=False,
        blank=False
    )

class Music(models.Model):
    name = models.CharField(
        verbose_name= 'Music Name',
        max_length=50,
        null=False,
        blank=False
    )
    url = models.URLField(
        verbose_name= 'Music Youtube URL',
        null=False,
        blank=True
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.SET('Deleted'),
        null=False,
        blank=False
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name= 'Music Tags',
        related_name= 'musics',
    )
