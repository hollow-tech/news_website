from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class News(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    text = models.TextField("Текст")
    image = models.ImageField("Изображение", upload_to='news/')
    tags = TaggableManager()
    slug = models.SlugField(max_length=130, unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
