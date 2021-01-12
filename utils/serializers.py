from rest_framework.serializers import ModelSerializer

class PatchModelSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(PatchModelSerializer,self).__init__(*args, **kwargs)