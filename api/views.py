from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import render
from api.models import User
from api.updatemodel import idList

# Create your views here.
class ApiUserListLV(ListView):
    model = User
    def get(self, request, *args, **kwargs):
        userList = []
        for user_id in idList:
            user = User.objects.get(id=user_id)
            user_dic = {"id":user_id, "rating":user.rating, "tier":user.tier}
            userList.append(user_dic)
        
        return JsonResponse(data=userList, safe=False)
