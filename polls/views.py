from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
#from django.views import generic
from .models import SubjectRegister, SubjectChoice

def index(request):
    subject_list = SubjectRegister.objects.order_by('id') #id순으로 보여줌.
    context = {'subject_list': subject_list}
    return render(request, 'polls/index.html', context)

def detail(request, subject_code_id):
    subject_code = get_object_or_404(SubjectRegister, pk=subject_code_id)
    return render(request, 'polls/polls_detail.html', {'subject_code': subject_code})

def results(request, subject_code_id):
    subject_code = get_object_or_404(SubjectRegister, pk=subject_code_id)
    return render(request, 'polls/polls_results.html', {'subject_code': subject_code})

def register(request):
    return render(request, 'polls/polls_register.html')

def vote(request, subject_code_id):
    question = get_object_or_404(SubjectRegister, pk=subject_code_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/polls_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def vote(request, subject_code):
#     return HttpResponse("You're voting on question %s." % subject_code)


# class RegisterView(generic.DeleteView):
#     model = SubjectRegister
#     template_name = 'polls/polls_register.html'

# class ChoiceView(generic.DeleteView):
#     model = SubjectChoice
#     template_name = 'polls/polls_choice.html'
