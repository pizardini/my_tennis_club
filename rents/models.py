from django.db import models
from members.models import Member
from equipments.models import Equipment

class Rent(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE, default=1)
  equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, default=1)
  rent_date = models.DateField(null=True)
  fee = models.IntegerField(null=True)


  def __str__(self):
    return f"{self.title}"
