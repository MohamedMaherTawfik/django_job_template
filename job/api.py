from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
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
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['title', 'vacancy','job_type',]
    search_fields = ['title', 'description',]
    ordering_fields = ['salary_start', 'salary_end','experince']

class jobdetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=job.objects.all()
    serializer_class=jobserializer    
    