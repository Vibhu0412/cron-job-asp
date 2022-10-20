from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import ChallengeStatementSerializer, ListRetrieveChallengeStatementSerializer
from .models import ChallengeStatement
from .permissions import IsChallengeCreator, IsOwner, IsManager
from .renderers import ChallengeCreatorRenderer
from rest_framework import status
from rest_framework.response import Response


# Create your views here
class ChallengeStatementViewSet(ModelViewSet):
    serializer_class = ChallengeStatementSerializer
    queryset = ChallengeStatement.objects.all().order_by('-created_at')
    # permission_classes = [IsAuthenticated, IsChallengeCreator | IsOwner]
    # permission_classes = [IsAuthenticated, IsChallengeCreator | IsManager]
    permission_classes = [IsAuthenticated, IsOwner]
    renderer_classes = [ChallengeCreatorRenderer]

    def create(self, request, *args, **kwargs):
        challenge_data = self.request.data
        challenge_data['user'] = self.request.user.id
        serializer = self.serializer_class(data=challenge_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Setting User to the Authenticated user
        request.data["user"] = self.request.user.id
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListRetrieveChallengeStatementSerializer(instance=instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        serializer = ListRetrieveChallengeStatementSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def list_my_challenges(self, request, *args, **kwargs):
        list_my_challenges_queryset= ChallengeStatement.objects.filter(user=request.user).order_by('-created_at')
        serializer = ListRetrieveChallengeStatementSerializer(list_my_challenges_queryset, many=True)
        return Response(serializer.data)







