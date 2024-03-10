from django.http import JsonResponse

def getRoute(request):
    routes = [
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return JsonResponse(routes, safe=False)