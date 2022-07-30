from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.
class ApiTodoLV(ListView):
    def get(self, request, *args, **kwargs):
        tmpList = ['역삼동원룸','천호동원룸','마포구원룸']
        return JsonResponse(data=tmpList, safe=False)
