from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # 👇 importante
    def get_serializer_context(self):
        return {"request": self.request}


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # 👇 importante
    def get_serializer_context(self):
        return {"request": self.request}
