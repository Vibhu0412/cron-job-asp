from rest_framework import serializers
from api.models import User
from .models import ChallengeStatement


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username',)


class ListRetrieveChallengeStatementSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ChallengeStatement
        fields = ['id', 'user', 'challenge_title', 'challenge_description', 'challenge_location', 'industry','skills',
                  'company_name','status', 'created_at']

class ChallengeStatementSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = ChallengeStatement
        fields = ['id', 'user', 'challenge_title', 'challenge_description', 'challenge_location', 'industry','skills',
                  'company_name','status', 'created_at']

