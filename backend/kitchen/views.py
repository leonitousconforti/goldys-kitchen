from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http import Http404

from django.core import serializers

from rest_framework import viewsets

from .models import *
from .serializers import *

class IngredientView(viewsets.ModelViewSet):
    serializer_class = IngredientsSerializer
    queryset = Ingredient.objects.all()

# class RecepieView(viewsets.ModelViewSet):
#     serializer_class = RecepieSerializer
#     queryset = Recepie.objects.all()
#
# class QuantityView(viewsets.ModelViewSet):
#     serializer_class = QuantitySerializer
#     queryset = Quantity.objects.all()


def index(request):
    ingredients = Ingredient.objects.all()
    template = loader.get_template('kitchen/index.html')
    context = {'ingredients': ingredients }

    return HttpResponse(template.render(context, request))

def detail(request, recepie_id):
    try:
        recepie = Recepie.objects.get(pk=recepie_id)
    except Recepie.DoesNotExist:
        raise Http404("Recepie Doesn't Exist")

    template = loader.get_template('kitchen/detail.html')
    context = {'recepie': recepie }

    return HttpResponse(template.render(context, request))
