# events app

# models.py

class Event(models.Model):
    # ... Event model fields ...
    pass

# serializers.py

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

# views.py

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# urls.py

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)