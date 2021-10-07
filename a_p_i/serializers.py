from rest_framework.serializers import (IntegerField, CharField, Serializer, ModelSerializer,
                                        HyperlinkedIdentityField)
from my_notes.models import MyNotes


class NoteSerializer(ModelSerializer):
    class Meta:
        model = MyNotes
        fields = '__all__' # все поля для отображения "id":, "title":, "text": и все остальные

#---------------------------------------настраиваемый сериалайзер------------------------------
#class ThinNoteSerializer(ModelSerializer):
    #url = HyperlinkedIdentityField(view_name='notes-detail') - очень ругалась Джанга на этот урл Х.З. почему (выяснить !!!!)
    #class Meta:
        #model = MyNotes
        #fields = ('id', 'title', 'url') # отобразит только выбранные поля

#-------------------------------------------------------------------
#class NoteSerializer(Serializer):
    #id = IntegerField(read_only=True)
    #title = CharField(required=True, max_length=250)
    #text = CharField(required=False, allow_blank=True)

    #def create(self, validated_data):
        #return MyNotes.objects.create(**validated_data)

    #def update(self, instance, validated_data):
        #instance.title = validated_data.get('title', instance.title)
        #instance.text = validated_data.get('text', instance.text)
        #instance.save()
        #return instance


