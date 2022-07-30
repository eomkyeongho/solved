from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

from solvedapp.models import Solvedapp

# Create your views here.
class SolvedappVueOnlyTV(TemplateView):
    template_name = 'solvedapp/solvedapp_vue_only.html'

class TodoCV(CreateView):
    model = Solvedapp
    fields = '__all__' # form에 필요한다는데?
    template_name = 'solvedapp/todo_form.html'
    success_url = reverse_lazy('solvedapp:list')

class TodoLV(ListView):
    model = Solvedapp
    template_name = 'solvedapp/todo_list.html'

class TodoDelV(DeleteView):
    model = Solvedapp
    template_name = 'solvedapp/todo_confirm_delete.html'
    success_url = reverse_lazy('solvedapp:list') # success_url 사용할 때는 대부분 reverse_lazy를 사용한다
