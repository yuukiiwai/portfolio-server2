from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict
from .models import History,Studystate,Strong,STUDYSTATE

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['when','event']

class _StudystatesSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        _to_representation = super().to_representation
        return [{
            statev[0]: _to_representation(Studystate.objects.filter(state = statev[0]))
            for statev in STUDYSTATE
        }]

    @property
    def data(self):
        return ReturnDict(super().data[0], serializer=self)

class StudystateSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = _StudystatesSerializer
        model = Studystate
        fields = ["imgurl","tech"]

class StrongSerializer(serializers.ModelSerializer):
    exps = serializers.StringRelatedField(many=True)

    class Meta:
        model = Strong
        fields = ['strong','exps']