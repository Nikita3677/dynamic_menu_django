from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40, unique=True)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title  = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='sub_category'
    )

    def __str__(self):
        return self.title