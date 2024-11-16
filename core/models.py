from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    team_position = models.IntegerField(default=0)  # changes by points


    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    


class Result(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    POSITION_CHOICES = [
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third'),
        ('Other', 'Other'),
    ]
    
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, default="First")
    position_rank = models.PositiveIntegerField(default=1, help_text="Rank among students with the same position")

    def __str__(self):
        return f"{self.program} - {self.student} ({self.position}, Rank: {self.position_rank})"


class Stage(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100) 
    program = models.ForeignKey(Program, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title



