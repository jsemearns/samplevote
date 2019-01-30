from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                    related_name='candidates',
                                    blank=True, null=True)
    birthdate = models.DateField()
    platform = models.TextField()

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE,
                                    related_name='votes')
    vote_datetime = models.DateTimeField(auto_now_add=True)
