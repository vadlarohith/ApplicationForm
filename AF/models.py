from django.db import models

class Application(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length = 50)
    Email = models.EmailField(max_length = 30)
    Age = models.IntegerField(max_length = 20)
    DateOfBirth = models.DateField(max_length = 10)

    def __str__(self):
        return self.Name
