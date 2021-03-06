from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=64, verbose_name="name")
    capacity = models.IntegerField(verbose_name="capacity")
    projector = models.BooleanField(verbose_name="projector")

class Reservation(models.Model):
    date = models.DateTimeField(verbose_name="date")
    room = models.ForeignKey(Room, verbose_name="room_id", on_delete=models.CASCADE, null=True)
    comment = models.TextField(verbose_name="comment")