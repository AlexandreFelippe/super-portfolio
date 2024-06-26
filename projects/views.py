from rest_framework import viewsets, permissions
from .models import Profile, Project, Certificate, CertifyingInstitution
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertificateSerializer,
    CertifyingInstitutionSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render


def index(request):
    context = {
        'profile': Profile.objects.get(pk=1),
        'projects': Project.objects.all(),
        'certificates': Certificate.objects.all(),
        'certifying_institutions': CertifyingInstitution.objects.all(),
    }
    print(Profile.objects.get(pk=1))
    print("_____________")
    return render(request, 'profile_detail.html', context)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == 'GET':
            profile = Profile.objects.get(pk=kwargs['pk'])
            return render(request, 'profile_detail.html', {
                'profile': profile,
                'certificates': profile.certificates.all(),
                'projects': profile.projects.all()
                })
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
