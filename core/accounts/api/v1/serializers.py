from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password


class RegistrationsSerializer(serializers.ModelSerializer):
    '''
    add fields to password2 in registration
    '''
    password2 = serializers.CharField(max_length=255 , write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password','password2']

    def validate(self, attrs):
        '''
        this is a function to validate the password and password2 field
        '''
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({'detail': 'passwords do not match'})
        
        try:
            validate_password(attrs.get('password'))

        except serializers.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password2', None)
        return User.objects.create_user(**validated_data)
