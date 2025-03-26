from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def item_list(request):
    search_query = request.GET.get('search', '')
    items = Item.objects.filter(name__icontains=search_query)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)

@api_view(['PUT'])
def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return Response(status=204)