# schedule app

# models.py
class Schedule(models.Model):
    # ... Schedule model fields ...
    pass

# serializers.py
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

# views.py
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# urls.py
router = routers.DefaultRouter()
router.register(r'schedule', ScheduleViewSet)