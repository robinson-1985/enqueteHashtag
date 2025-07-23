from django.http import HttpResponse


def index(request):
    return HttpResponse("Seja bem vindo à enquete")


def results(request, question_id):
    return HttpResponse(f"Você está vendo os resultados da pergunta {question_id}")
