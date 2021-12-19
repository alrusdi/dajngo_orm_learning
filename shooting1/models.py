from django.db import models


class City(models.Model):
    name = models.CharField(title="Название города", max_length=255, unique=True)

    def __repr__(self):
        return f"City: {self.name}"


class Shooter(models.Model):
    name = models.CharField(title="Фамилия и имя игрока", max_length=255, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __repr__(self):
        return f"Shooter: {self.name}"


class Result(models.Model):
    shooter = models.ForeignKey(Shooter, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()  # Количество очков набранных данным стрелком

    def __repr__(self):
        return f"Result: {self.shooter.name} {self.score}"
