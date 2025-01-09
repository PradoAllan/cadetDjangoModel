from django.db import models

class   Roles(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=254)

class   Cadet(models.Model):
    intra_id = models.BigIntegerField()
    username = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
    about = models.CharField(max_length=254)
    presentation_video = models.URLField()
    #Urlflield tem como max_lenght default = 200
    #presentation_video = models.TextField() # nao tem um limite, parece
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

