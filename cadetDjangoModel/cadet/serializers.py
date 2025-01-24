# from rest_framework import serializers
# from .models import Cadet, Roles

# class   CadetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cadet
#         fields = '__all__'

# class   RolesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Roles
#         fields = '__all__'


from .models import User, Role, UserIntra, WorkExperience, WorkTitle
from rest_framework import serializers

class   UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class   RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class   UserIntraSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIntra
        fields = '__all__'

# class   UserPersonalProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserPersonalProject
#         fields = '__all__'

# class   UserPraticalProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserPraticalProject
#         fields = '__all__'

# class   UserSkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserSkill
#         fields = '__all__'

class   WorkExperienceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class   WorkTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTitle
        fields = '__all__'

# class   AdditionalProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdditionalProject
#         fields = '__all__'

# class   LanguageLevelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LanguageLevel
#         fields = '__all__'

# class   SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Skill
#         fields = '__all__'