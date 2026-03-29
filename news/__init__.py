# news app

# models.py
class News(models.Model):
    # ... News model fields ...
    pass

# serializers.py
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

# views.py
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# urls.py
router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)