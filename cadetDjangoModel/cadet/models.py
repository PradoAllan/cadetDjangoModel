from django.db import models

class   UserIntra(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60)
    intra_id = models.CharField(max_length=60)
    project_id = models.IntegerField()
    presence_id = models.IntegerField()
    # alumini = models.BooleanField(default=False)
    # aluminized_at = models.DateTimeField(blank=True, null=True)

class   WorkTitle(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)

class   WorkExperience(models.Model):
    id = models.AutoField(primary_key=True)
    # company_id = models.ForeignKey(blank=False, on_delete=models.CASCADE, related_name="user")
    company_id = models.IntegerField(blank=True) # need relate this field to the company model
    title_id = models.ForeignKey(WorkTitle, blank=True, null=True, on_delete=models.SET_NULL, related_name="work_experience")
    title = models.CharField(max_length=60)
    # OneToOneRel(WorkTitle, blank=False, on_delete=models.SET_NULL) 
    started_at = models.DateTimeField(blank=False, editable=True) # need to check how this is done
    ended_at = models.DateTimeField(blank=False, editable=True)
    work_type = models.CharField(max_length=60) #enum
    location = models.CharField(max_length=60)
    location_type = models.CharField(max_length=60) #enum
    description = models.TextField(blank=True)

# class   LanguageLevel(models.Model):
#     id = models.AutoField(primary_key=True)
#     language = models.CharField(max_length=60)

# class   Skill(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=60)

# class   UserSkill(models.Model):
#     id = models.AutoField(primary_key=True)
#     skill_id = models.ForeignKey(Skill, blank=False, on_delete=models.CASCADE, related_name="user_skill")
#     type = models.CharField(max_length=254)
#     level_id = models.ForeignKey(LanguageLevel, blank=False, on_delete=models.CASCADE, related_name="user_level")
#     certificate_id = models.URLField(max_length=254)

# class   UserPersonalProject(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=60)
#     description = models.TextField(blank=True)
#     link = models.URLField(max_length=254)
#     img = models.URLField(max_length=254)
#     repository_url = models.URLField(max_length=254)

# class   AdditionalProject(models.Model):
#     id = models.AutoField(primary_key=True)
#     # project_id ??
#     title = models.CharField(max_length=60)
#     description = models.TextField(blank=True)
#     type = models.CharField(max_length=60, blank=True)
#     creator_type = models.CharField(max_length=60, blank=True)
#     completion_time = models.PositiveIntegerField(default=0) # Change to max completion time and remove default

# class   UserPraticalProject(models.Model):
#     id = models.AutoField(primary_key=True)
#     additional_project = models.OneToOneField(AdditionalProject, blank=False, on_delete=models.CASCADE, related_name="additional_project")
#     # pratical_project_id ??
#     repository_url = models.URLField(max_length=254)
#     started_at = models.DateTimeField(blank=False, editable=True)


class   Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=254)

class   User(models.Model):
    id = models.AutoField(primary_key=True)
    user_intra_id = models.ForeignKey(UserIntra, blank=True, null=True, on_delete=models.CASCADE, related_name="user")
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    role_name = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL, related_name="users")
    about = models.TextField(blank=True)
    presentation_video = models.URLField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    work_experience = models.ForeignKey(WorkExperience, blank=True, null=True, on_delete=models.CASCADE, related_name="user_work_experience")
    # user_skill = models.ForeignKey(UserSkill, blank=True, on_delete=models.CASCADE, related_name="user_skill")
    # personal_project = models.ForeignKey(UserPersonalProject, blank=True, on_delete=models.CASCADE, related_name="user_personal_project")
    # additional_project = models.ForeignKey(UserPraticalProject, blank=True, on_delete=models.CASCADE, related_name="user_additional_project")

