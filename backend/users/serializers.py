from django.contrib.auth import get_user_model
from rest_framework import serializers

User=get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_active', ]
        read_only_fields = ['id', 'role', ]

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer pour l'inscription d'un nouvel utilisateur.
    lire des infor d'un utilisateur (jamais le mot de passe)
    """
    password = serializers.CharField(write_only=True,min_length=12)
    
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        """
        Créer et sauvegarder un nouvel utilisateur.
        """
        return User.objects.create_user(**validated_data)
    