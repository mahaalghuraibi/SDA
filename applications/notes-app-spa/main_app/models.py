from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=250)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


MEALS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night'),
)


class MoodCheck(models.Model):
    date = models.DateField('Mood check date')
    period = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_period_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.TextField()
    title = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    note = models.OneToOneField(Note, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for note_id: {self.note.id} @{self.url}"

