from django.shortcuts import render


def results(request, question_id):
    # Sua lógica de visualização aqui
    return render(request, 'polls/results.html', {'question_id': question_id})
