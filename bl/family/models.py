from django.db import models
# Create your models here.


class member(models.Model):
    name=models.CharField('名字',max_length=100)

class Country(models.Model):
    name=models.CharField(max_length=200)
    continent=models.CharField(max_length=200)

class Article(models.Model):
    articletype=(
        ('Study','留学'),
        ('Travel','旅行'),
    )

    title = models.CharField(max_length=200, unique=True)
    edittime=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=200,choices=articletype,default='留学')

    img = models.ImageField(upload_to='blog_images', null=True, blank=True, verbose_name='博客配图')

    def __str__(self):
        return self.title

    class Meta:

        ordering=['-edittime']
        verbose_name='文章'
        verbose_name_plural='文章'





