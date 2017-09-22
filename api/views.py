from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import TiposAtributos
from api.serializers import TiposAtributosSerializer

@csrf_exempt
def tipos_atributos_list(request):
    if request.method == 'GET':
        tipos_atributos = TiposAtributos.objects.all()
        serializer = TiposAtributosSerializer(tipos_atributos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TiposAtributosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def tipos_atributos_detail(request, pk):
    try:
        tipos_atributos = TiposAtributos.objects.get(pk=pk)
    except TiposAtributos.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TiposAtributosSerializer(tipos_atributos)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TiposAtributosSerializer(tipos_atributos, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        tipos_atributos.delete()
        return HttpResponse(status=204)