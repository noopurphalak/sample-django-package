from django.http import JsonResponse

# Create your views here.


def hello(request):
    return JsonResponse({"greeting": "Hello World"})
