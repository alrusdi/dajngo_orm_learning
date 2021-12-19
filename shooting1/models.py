from django.db import models


class City(models.Model):
    name = models.CharField(verbose_name="Название города", max_length=255, unique=True)

    def __str__(self):
        return f"City: {self.name}"


class Shooter(models.Model):
    name = models.CharField(verbose_name="Фамилия и имя игрока", max_length=255, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"Shooter: {self.name}"


class Result(models.Model):
    shooter = models.ForeignKey(Shooter, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(verbose_name="Количество очков")

    def __str__(self):
        return f"Result: {self.shooter.name} {self.score}"
