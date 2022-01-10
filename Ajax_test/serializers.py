from Ajax_test.models import ActualWork
from rest_framework import serializers
from .models import ActualWork,Matter

class ActualWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActualWork
        fields = '__all__'

    def makeData(ActualWork, Matter):
        
        return 
