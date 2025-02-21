from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=50)
    responsible = models.CharField(max_length=50,)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.__all__

class Stages(models.Model):
    projectId = models.IntegerField()
    name = models.CharField(max_length=50)
    position = models.IntegerField()

    def __str__(self):
        return self.__all__

class Tasks(models.Model):
    projectId = models.IntegerField()
    stageId = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256, blank=True)
    responsible = models.CharField(max_length=50)
    position = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.__all__
