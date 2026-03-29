# professors app

# models.py
class Professor(models.Model):
    # ... Professor model fields ...
    pass

# serializers.py
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

# views.py
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

# urls.py
router = routers.DefaultRouter()
router.register(r'professors', ProfessorViewSet)