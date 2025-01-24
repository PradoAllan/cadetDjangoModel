from django.db import models

# class   Roles(models.Model):
#     name = models.CharField(max_length=60)
#     description = models.CharField(max_length=254)

class   Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=254)

# class   Cadet(models.Model):
#     intra_id = models.BigIntegerField()
#     username = models.CharField(max_length=60)
#     name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     email = models.EmailField(max_length=254)
#     role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
#     about = models.CharField(max_length=254)
#     presentation_video = models.URLField()
#     #Urlflield tem como max_lenght default = 200
#     #presentation_video = models.TextField() # nao tem um limite, parece
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class   User(models.Model):
    id = models.AutoField(primary_key=True)
    # user_intra_id = models.ForeignKey(UserIntra, on_delete=models.CASCADE, related_name="user")
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    role_name = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL, related_name="users")
    about = models.TextField(blank=True)
    presentation_video = models.URLField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # work_experience = models.ForeignKey(WorkExperience, blank=True, on_delete=models.CASCADE, related_name="user_work_experience")
    # user_skill = models.ForeignKey(UserSkill, blank=True, on_delete=models.CASCADE, related_name="user_skill")
    # personal_project = models.ForeignKey(UserPersonalProject, blank=True, on_delete=models.CASCADE, related_name="user_personal_project")
    # additional_project = models.ForeignKey(UserPraticalProject, blank=True, on_delete=models.CASCADE, related_name="user_additional_project")

