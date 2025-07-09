from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=128)
    code = models.SlugField(max_length=16, unique=True, blank=True)

    def __str__(self):
        return self.name

    def count_products(self):
        return self.products.count()

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=128)
    code = models.SlugField(max_length=16, unique=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    pubdate = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()

    def avg_rate(self):
        rate = [comment.rate for comment in self.comments.all()]
        if rate:
            return sum(rate) / len(rate)
        return 0

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.code:
            num_for_slug = f'{self.id:04}'
            self.code = (
                f'{slugify(self.category)}-'
                f'{slugify(self.name)}-'
                f'{num_for_slug}'
            )
            Product.objects.filter(pk=self.pk).update(code=self.code)


RATES = (
    (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
)


class Comment(models.Model):
    text = models.TextField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pubdate = models.DateField(auto_now_add=True)
    rate = models.IntegerField(choices=RATES)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text
