#-*- coding: utf-8 -*-
from .forms import ProfileForm
from .models import Profile
from django.shortcuts import render

def SaveProfile(request):
   saved = False   
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      
      if MyProfileForm.is_valid():
         profile = Profile()
         profile.name = MyProfileForm.cleaned_data["name"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
   else:
      MyProfileForm = ProfileForm()
		
   return render(request, 'saved.html',{'form': MyProfileForm})