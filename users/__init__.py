# users app

# models.py
class User(models.Model):
    # ... User model fields ...
    pass

# serializers.py
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# views.py
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# urls.py
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)