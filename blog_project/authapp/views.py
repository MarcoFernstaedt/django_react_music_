from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, ProfileSerializer
from .models import Profile

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            "user": UserRegistrationSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Email Verification process."
        }, status=status.HTTP_201_CREATED)
    
class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_serializer_context(self):
        return {'request': self.request}