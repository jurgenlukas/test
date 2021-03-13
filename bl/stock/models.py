from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
from PIL import Image



class member(models.Model):
    name=models.CharField('名字',max_length=100)

class Country(models.Model):
    name=models.CharField(max_length=200)
    continent=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    name=models.CharField(max_length=100)


class Article(models.Model):
    articletype=(
        ('Study','留学'),
        ('Travel','旅行'),
    )
    country = models.ForeignKey(
        Country,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='Country'
    )
    title = models.CharField(max_length=200, unique=True)
    content=models.CharField(max_length=500)
    edittime=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=200,choices=articletype,default='留学')

    img= models.ImageField(upload_to='blog_images/', null=True,blank=True)

    def save(self, *args, **kwargs):
        # 调用原有的 save() 的功能
        article = super(Article, self).save(*args, **kwargs)

        # 固定宽度缩放图片大小
        if self.img and not kwargs.get('update_fields'):
            image = Image.open(self.img)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.img.path)

        return article

    def __str__(self):
        return self.title

    class Meta:

        ordering=['-edittime']
        verbose_name='文章'
        verbose_name_plural='文章'





