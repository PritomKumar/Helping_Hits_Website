from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import URLValidator
from sklearn.tree import DecisionTreeClassifier
import joblib
from .import predictor


# Create your models here.


class Data(models.Model):
    # song_url = models.CharField(max_length=1000, null=True)
    song_url = models.URLField(max_length=1000, blank=True, null=True)
    predictions = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        playlists = predictor.predict_songs(self.song_url)
        self.predictions = playlists
        # self.predictions = 'special prediction = ' + self.song_url
        return super().save(*args, *kwargs)

    def __str__(self):
        return self.song_url


# GENDER = (
#     (0, 'Female'),
#     (1, 'Male'),
# )


# class Data(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     age = models.PositiveIntegerField(
#         validators=[MinValueValidator(13), MaxValueValidator(19)], null=True)
#     height = models.PositiveIntegerField(null=True)
#     sex = models.PositiveIntegerField(choices=GENDER, null=True)
#     predictions = models.CharField(max_length=100, blank=True)
#     date = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         ml_model = joblib.load('ml_model/ml_sport_model.joblib')
#         self.predictions = ml_model.predict(
#             [[self.age, self.height, self.sex]])
#         return super().save(*args, *kwargs)

#     class Meta:
#         ordering = ['-date']

#     def __str__(self):
#         return self.name
