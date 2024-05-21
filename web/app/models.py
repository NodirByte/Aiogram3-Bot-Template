from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, help_text='Enter your name')
    telegram_id = models.CharField(max_length=100, null=True, blank=True, help_text='Enter your telegram id')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'