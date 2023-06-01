from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    discord_id = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    nickname = models.TextField(blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)
    roles = models.TextField(blank=True, null=True)
    joined = models.TextField(blank=True, null=True)
    access = models.TextField(blank=True, null=True)
    last_login = models.DateField()

    def is_authenticate(self,request):
        return True

    class Meta:
        managed = False
        db_table = 'users'