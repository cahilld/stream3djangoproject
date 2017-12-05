from django.db import models

statuschoice = (
                ('P', 'Pending'),
                ('I', 'In Process'),
                ('D', 'Done'),
                ('A', 'Abandoned')
              )

# Create your models here.
class TodoItem(models.Model):
    name = models.CharField(max_length=80, blank=False)
    description = models.TextField(max_length=350)
    owner = models.ForeignKey('auth.User')
    status = models.CharField(max_length=1, choices=statuschoice, default='P')

    def __str__(self):
        return self.name