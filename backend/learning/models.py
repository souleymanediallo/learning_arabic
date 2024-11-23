from django.db import models
from django.conf import settings
import uuid

from django.utils.text import slugify


# Create your models here.
class Tome(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Tome, self).save(*args, **kwargs)

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    tome = models.ForeignKey(Tome, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Lesson, self).save(*args, **kwargs)


class Word(models.Model):
    arabic_word = models.CharField(max_length=200)
    french_word = models.CharField(max_length=200)
    quiz_success = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.arabic_word} - {self.french_word}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.french_word)
        super(Word, self).save(*args, **kwargs)


class QuizHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="quiz_histories")
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="quiz_histories")
    is_correct = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.first_name} - {self.word.french_word} - {'Correct' if self.is_correct else 'Incorrect'}"


class QuizScore(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="quiz_score")
    total_attempts = models.PositiveIntegerField(default=0)
    total_correct = models.PositiveIntegerField(default=0)
    total_incorrect = models.PositiveIntegerField(default=0)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} - Correct: {self.total_correct}, Incorrect: {self.total_incorrect}"

    def update_score(self, is_correct):
        self.total_attempts += 1
        if is_correct:
            self.total_correct += 1
        else:
            self.total_incorrect += 1
        self.save()