from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __repr__(self):
        return f"City: {self.name}"


class Shooter(models.Model):
    name = models.CharField(max_length=255, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Result(models.Model):
    shooter = models.ForeignKey(Shooter, on_delete=models.CASCADE)
    result = models.PositiveIntegerField()
