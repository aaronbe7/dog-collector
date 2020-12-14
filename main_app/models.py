from django.db import models
from django.urls import reverse
from datetime import date

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'dog_id': self.id})

  def walked_for_today(self):
    return self.walking_set.filter(date=date.today()).count() >= len(TIMES)

class Walking(models.Model):
  date = models.DateField('walking date')
  time = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0] 
  )
  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_time_display()} on {self.date}"

  class Meta:
    ordering = ['-date']