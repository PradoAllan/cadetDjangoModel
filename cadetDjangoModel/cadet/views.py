from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse

from rest_framework import status

from .models import User, Role
from .serializers import UserSerializer, RoleSerializer

# from .models import User, Role, UserPersonalProject, UserPraticalProject, AdditionalProject, LanguageLevel, Skill, UserSkill, WorkTitle, WorkExperience
# from .serializers import UserSerializer, RoleSerializer, UserPersonalProjectSerializer, UserPraticalProjectSerializer, AdditionalProjectSerializer, LanguageLevelSerializer, SkillSerializer, UserSkillSerializer, WorkTitleSerializer, WorkExperienceSerilizer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# ------------------ USER'S ROUTE ------------------
class   UserAPIView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serializer.validated_data
        serializer.create(valid_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class   UserIdAPIView(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serializer.validated_data
        serializer.update(user, valid_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except:
            return Response({"Error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        User.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------ ROLE'S ROUTE ------------------
class   RoleAPIView(APIView):
    def get(self, request):
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serializer.validated_data
        serializer.create(valid_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class   RoleIdAPIView(APIView):
    def get(self, request, pk):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serializer.validated_data
        serializer.update(role, valid_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        try:
            role = Role.objects.get(id=pk)
        except:
            return Response({"Error": "Role not found."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = RoleSerializer(role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        Role.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# # ------------------ WORKEXPERIENCE'S ROUTE ------------------
# # WorkExperienceSerilizer  Get/Post/Put/Patch/Delete
# class   WorkExperienceAPIView(APIView):
#     def get(self, request):
#         workExperience = WorkExperience.objects.all()
#         serialized = WorkExperienceSerilizer(workExperience, many=True)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def post(self, request):
#         serialized = WorkExperienceSerilizer(request.data)
#         if not serialized.is_valid():
#             return (Response(serialized.erros, status=status.HTTP_400_BAD_REQUEST))
#         valid = serialized.validated_data
#         serialized.create(valid)
#         return (Response(serialized.data, status=status.HTTP_201_CREATED))

# class   WorkExperienceIdAPIView(APIView):
#     def get(self, request, pk):
#         workExperience = WorkExperience.objects.get(id=pk)
#         serialized = WorkExperienceSerilizer(workExperience)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def patch(self, request, pk):
#         try:
#             workExperience = WorkExperience.objects.get(id=pk)
#         except:
#             return Response({"Error": "Work experience not found."}, status=status.HTTP_400_BAD_REQUEST)
#         serialized = WorkExperienceSerilizer(workExperience, data=request.data, partial=True)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         WorkExperience.objects.filter(id=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # ------------------ WORKTITLE'S ROUTE ------------------
# # WorkTitleSerializer, Get/Post/Put/Patch/Delete
# class   WorkTitleAPIView(APIView):
#     def get(self, request):
#         workTitle = WorkTitle.objects.all()
#         serialized = WorkTitleSerializer(workTitle, many=True)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def post(self, request):
#         serialized = WorkTitleSerializer(request.data)
#         if not serialized.is_valid():
#             return (Response(serialized.erros, status=status.HTTP_400_BAD_REQUEST))
#         valid = serialized.validated_data
#         serialized.create(valid)
#         return (Response(serialized.data, status=status.HTTP_201_CREATED))

# class   WorkTitleIdAPIView(APIView):
#     def get(self, request, pk):
#         workTitle = WorkTitle.objects.get(id=pk)
#         serialized = WorkTitleSerializer(workTitle)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def patch(self, request, pk):
#         try:
#             workTitle = WorkTitle.objects.get(id=pk)
#         except:
#             return Response({"Error": "Work title not found."}, status=status.HTTP_400_BAD_REQUEST)
#         serialized = WorkTitleSerializer(workTitle, data=request.data, partial=True)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         WorkTitle.objects.filter(id=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # ------------------ USERPERSONALPROJECT'S ROUTE ------------------
# # UserPersonalProjectSerializer,  Post/Put/Patch/Delete
# class   UserPersonalProjectAPIView(APIView):
#     def post(self, request):
#         serialized = UserPersonalProjectSerializer(request.data)
#         if not serialized.is_valid():
#             return (Response(serialized.erros, status=status.HTTP_400_BAD_REQUEST))
#         valid = serialized.validated_data
#         serialized.create(valid)
#         return (Response(serialized.data, status=status.HTTP_201_CREATED))

# class   UserPersonalProjectIdAPIView(APIView):
#     def get(self, request, pk):
#         userPersonalProject = UserPersonalProject.objects.get(id=pk)
#         serialized = UserPersonalProjectSerializer(userPersonalProject)
#         return (Response(userPersonalProject, status=status.HTTP_200_OK))
    
#     def patch(self, request, pk):
#         try:
#             userPresonalProject = UserPersonalProject.objects.get(id=pk)
#         except:
#             return Response({"Error": "User personal project not found."}, status=status.HTTP_400_BAD_REQUEST)
#         serialized = UserPersonalProjectSerializer(userPresonalProject, data=request.data, partial=True)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         UserPersonalProject.objects.filter(id=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # ------------------ USERPRATICALPROJECT'S ROUTE ------------------
# # UserPraticalProjectSerializer, Get/Post/Put/Patch/Delete
# class   UserPraticalProjectAPIView(APIView):
#     def get(self, request):
#         userPraticalProject = UserPraticalProject.objects.all()
#         serialized = UserPraticalProjectSerializer(userPraticalProject, many=True)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def post(self, request):
#         serialized = UserPraticalProjectSerializer(request.data)
#         if not serialized.is_valid():
#             return (Response(serialized.erros, status=status.HTTP_400_BAD_REQUEST))
#         valid = serialized.validated_data
#         serialized.create(valid)
#         return (Response(serialized.data, status=status.HTTP_201_CREATED))

# class   UserPraticalProjectIdAPIView(APIView):
#     def get(self, request, pk):
#         userPraticalProject = UserPraticalProject.objects.get(id=pk)
#         serialized = UserPraticalProjectSerializer(userPraticalProject)
#         return (Response(serialized.data, status=status.HTTP_200_OK))

#     def patch(self, request, pk):
#         try:
#             userPraticalProject = UserPraticalProject.objects.get(id=pk)
#         except:
#             return Response({"Error": "User pratical project not found."}, status=status.HTTP_400_BAD_REQUEST)
#         serialized = UserPraticalProjectSerializer(userPraticalProject, data=request.data, partial=True)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         UserPraticalProject.objects.filter(id=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # ------------------ AdditionalPROJECT'S ROUTE ------------------
# # AdditionalProjectSerializer, Get/Post/Put/Patch/Delete
# class   AdditionalProjectAPIView(APIView):
#     def get(self, request):
#         additionalProject = AdditionalProject.objects.all()
#         serialized = AdditionalProjectSerializer(additionalProject, many=True)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def post(self, request):
#         serialized = AdditionalProjectSerializer(request.data)
#         if not serialized.is_valid():
#             return (Response(serialized.erros, status=status.HTTP_400_BAD_REQUEST))
#         valid = serialized.validated_data
#         serialized.create(valid)
#         return (Response(serialized.data, status=status.HTTP_201_CREATED))

# class   AdditionalProjectIdAPIView(APIView):
#     def get(self, request, pk):
#         additionalProject = AdditionalProject.objects.get(id=pk)
#         serialized = AdditionalProjectSerializer(additionalProject, many=True)
#         return (Response(serialized.data, status=status.HTTP_200_OK))

#     def patch(self, request, pk):
#         try:
#             additionalProject = AdditionalProject.objects.get(id=pk)
#         except:
#             return Response({"Error": "additional project not found."}, status=status.HTTP_400_BAD_REQUEST)
#         serialized = AdditionalProjectSerializer(additionalProject, data=request.data, partial=True)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         AdditionalProject.objects.filter(id=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # ------------------ LANGUAGELEVEL'S ROUTE ------------------
# # LanguageLevelSerializer, Get/Post/Put/Patch/Delete
# class   LanguageLevelAPIView(APIView):
#     def get(self, request):
#         languageLevel = LanguageLevel.objects.all()
#         serialized = LanguageLevelSerializer(languageLevel, many=True)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def post(self, request):
#         serialized = LanguageLevelSerializer(request.data)
#         if not serialized.is_valid():
#             return (Response(serialized.erros, status=status.HTTP_400_BAD_REQUEST))
#         valid = serialized.validated_data
#         serialized.create(valid)
#         return (Response(serialized.data, status=status.HTTP_201_CREATED))

# class   LanguageLevelIdAPIView(APIView):
#     def get(self, request, pk):
#         languageLevel = LanguageLevel.objects.get(id=pk)
#         serialized = LanguageLevelSerializer(languageLevel, many=True)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def patch(self, request, pk):
#         try:
#             languageLevel = LanguageLevel.objects.get(id=pk)
#         except:
#             return Response({"Error": "language level not found."}, status=status.HTTP_400_BAD_REQUEST)
#         serialized = LanguageLevelSerializer(languageLevel, data=request.data, partial=True)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         LanguageLevel.objects.filter(id=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # ------------------ SKILL'S ROUTE ------------------
# # SkillSerializer, Get/Post/Put/Patch/Delete
# class   SkillAPIView(APIView):
#     def get(self, request):
#         skill = Skill.objects.all()
#         serialized = SkillSerializer(skill, many=True)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def post(self, request):
#         serialized = SkillSerializer(request.data)
#         if not serialized.is_valid():
#             return (Response(serialized.erros, status=status.HTTP_400_BAD_REQUEST))
#         valid = serialized.validated_data
#         serialized.create(valid)
#         return (Response(serialized.data, status=status.HTTP_201_CREATED))

# class   SkillIdAPIView(APIView):
#     def get(self, request, pk):
#         skill = Skill.objects.get(id=pk)
#         serialized = SkillSerializer(skill, many=True)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def patch(self, request, pk):
#         try:
#             skill = Skill.objects.get(id=pk)
#         except:
#             return Response({"Error": "skill not found."}, status=status.HTTP_400_BAD_REQUEST)
#         serialized = SkillSerializer(skill, data=request.data, partial=True)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         Skill.objects.filter(id=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # ------------------ USERSKILL'S ROUTE ------------------
# # UserSkillSerializer, Get/Post/Put/Patch/Delete
# class   UserSkillAPIView(APIView):
#     def get(self, request):
#         userSkill = UserSkill.objects.all()
#         serialized = UserSkillSerializer(userSkill, many=True)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def post(self, request):
#         serialized = UserSkillSerializer(request.data)
#         if not serialized.is_valid():
#             return (Response(serialized.erros, status=status.HTTP_400_BAD_REQUEST))
#         valid = serialized.validated_data
#         serialized.create(valid)
#         return (Response(serialized.data, status=status.HTTP_201_CREATED))

# class   UserSkillIdAPIView(APIView):
#     def get(self, request, pk):
#         userSkill = UserSkill.objects.get(id=pk)
#         serialized = UserSkillSerializer(userSkill, many=True)
#         return (Response(serialized.data, status=status.HTTP_200_OK))
    
#     def patch(self, request, pk):
#         try:
#             userSkill = UserSkill.objects.get(id=pk)
#         except:
#             return Response({"Error": "user skill not found."}, status=status.HTTP_400_BAD_REQUEST)
#         serialized = UserSkillSerializer(userSkill, data=request.data, partial=True)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         UserSkill.objects.filter(id=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class   CadetListCreateAPIView(APIView):
#     def get(self, request):
#         cadets = Cadet.objects.all()
#         serialized = CadetSerializer(cadets, many=True)
#         return Response(serialized.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serialized = CadetSerializer(data=request.data)
#         if not serialized.is_valid():
#             return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
#         valid_data = serialized.validated_data
#         serialized.create(valid_data)
#         return Response(serialized.data, status=status.HTTP_201_CREATED)

# class   CadetRetrieveUpdateDeleteAPIView(APIView):
#     def get(self, request, pk):
#         cadet = Cadet.objects.get(id=pk)
#         serialized = CadetSerializer(cadet)
#         return Response(serialized.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         cadet = Cadet.objects.get(id=pk)
#         serializer = CadetSerializer(data=request.data)

#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         validated_data = serializer.validated_data
#         serializer.update(cadet, validated_data)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def patch(self, request, pk):
#         try:
#             cadet = Cadet.objects.get(id=pk)
#         except:
#             return Response({"error": "Cadet not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = CadetSerializer(cadet, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         Cadet.objects.filter(id=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class   RolesListCreateAPIView(APIView):
#     def get(self, request):
#         roles = Roles.objects.all()
#         serialized = RolesSerializer(roles, many=True)
#         return Response(serialized.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serialized = RolesSerializer(data=request.data)
#         if not serialized.is_valid():
#             return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
#         valid_data = serialized.validated_data
#         serialized.create(valid_data)
#         return Response(serialized.data, status=status.HTTP_200_OK)

# class   RolesRetrieveUpdateDeleteAPIView(APIView):
#     def get(self, request, pk):
#         role = Roles.objects.get(id=pk)
#         serialized = RolesSerializer(role)
#         return Response(serialized.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         role = Roles.objects.get(id=pk)
#         serializer = RolesSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         valid_data = serializer.validated_data
#         serializer.update(role, valid_data)
#         return Response(serializer.data, role)

#     def patch(self, request, pk):
#         try:
#             role = Roles.objects.get(id=pk)
#         except Roles.DoesNotExist:
#             return Response({"error": "Role not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = RolesSerializer(role, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         Roles.objects.filter(id=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# #EXEMPLE PATH METHOD:
# #  def patch(self, request, item_id): 
# #      try:
# #         #Retrieve the item by Id 
# #         item = Item.objects.get(id=item_id) 
# #      except Item.DoesNotExist:
# #             return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
# #      #Partially update with incoming data serializer Itemserializer(item, data-request.data, partial-True)
# #       if serializer.is_valid():

# #         #Save only the fields provided 
# #         serializer.save()
# #         return Response(serializer.data, status=status.HTTP_280_OK)

# #      else:
# #         return Response(sertalizer.errors,status=status.HTTP_400_BAD_REQUEST)

# # @api_view(['GET', 'POST'])
# # def cadetView(request):
# #     if request.method == 'GET':
# #         cadet = Cadet.objects.all()
# #         serializer = CadetSerializer(cadet, many=True)

# #         return Response(serializer.data, status=status.HTTP_200_OK)
# #         #return HttpResponse(serializer.data)
# #     elif request.method == 'POST':
# #         serializer = CadetSerializer(data=request.data)
# #         if not serializer.is_valid():
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #         validated_data = serializer.validated_data
# #         serializer.create(validated_data)
# #         return Response(serializer.data, status=status.HTTP_201_CREATED)


# # @api_view(['GET', 'POST'])
# # def RolesView(request):
# #     if request.method == 'GET':
# #         roles = Roles.objects.all()
# #         serializer = RolesSerializer(roles, many=True)

# #         return Response(serializer.data, status=status.HTTP_200_OK)
# #     elif request.method == 'POST':
# #         serializer = RolesSerializer(data=request.data)
# #         if not serializer.is_valid():
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #         validated_data = serializer.validated_data
# #         serializer.create(validated_data)
# #         return Response(serializer.data, status=status.HTTP_201_CREATED)