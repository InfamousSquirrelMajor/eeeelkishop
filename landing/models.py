from django.db import models

# Create your models here.
class Profile(models.Model):
    email = models.EmailField()
   

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'