from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import talk
from .serializers import talkSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def talk_list(request):
    if request.method == 'GET':
        talks = talk.objects.all().order_by('-id')
        serializer = talkSerializer(talks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = talkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Post created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)