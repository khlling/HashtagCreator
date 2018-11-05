from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .fileHandler import hashtag

@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse("To use this service make POST request to: http://127.0.0.1:8000/hashtag/")
    elif request.method == 'POST':
        body = json.loads(request.body)
        return JsonResponse(hashtag.generator().generate(body['filePath'], body['noResults'], body['model']),
                            safe=False)

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

