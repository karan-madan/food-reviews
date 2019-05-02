from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post1(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post2(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post3(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post4(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post5(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post6(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post7(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post8(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post9(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post10(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post11(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post12(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post13(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post14(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post15(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post16(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post17(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post18(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post19(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


