from django.db import models

class articles(models.Model):
    title = models.CharField('Name', max_length=100)
    anons = models.CharField('Anounsment', max_length=250)
    full_text = models.TextField('Note')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return  f'/news/{self.id}'
# Create your models here.
