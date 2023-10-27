
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import jobserializer
from .models import job

# @api_view(['GET'])
# def job_list_api(request):
#     jobs=job.objects.all()
#     data=jobserializer(jobs,many=True).data
#     return Response({'Jobs':data})

# @api_view(['GET'])
# def job_dateail_api(request,id):
#     jobe=job.objects.get(id=id)
#     data=jobserializer(jobe).data
#     return Response({'Job':data})



class joblistapi(generics.ListCreateAPIView):
    queryset=job.objects.all()
    serializer_class=jobserializer



class jobdetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=job.objects.all()
    serializer_class=jobserializer    