from rest_framework.serializers import (IntegerField, CharField, Serializer, ModelSerializer,
                                        HyperlinkedIdentityField, SerializerMethodField)
from my_notes.models import MyNotes


class NoteSerializer(ModelSerializer):
    author = SerializerMethodField(read_only=False)
    def get_author(self, obj):
        return obj.author.username #в JSON формате записи отображаеться имя автора записи "author" : "name"

    class Meta:
        model = MyNotes
        fields = '__all__' # все поля для отображения "id":, "title":, "text": и все остальные


#------------------урок 28---------------------делаем сериалайзер для возможности добавления юзеров по API------------------------------

from django.contrib.auth import get_user_model
class UserSerializer(ModelSerializer):

    class Meta:
        model = get_user_model() #функция которая возвращает модель текущего юзера
        queryset = model.objects.all()
        fields = ('id', 'email', 'password', 'username', 'is_superuser', 'is_staff')
        extra_kwargs = {'password': {'write_only':True}}
    def create(self, validated_data):
        user = self.Meta.model(**validated_data) #распаковка словаря
        user.set_password(validated_data.pop('password', '')) # - добавил сам из-за возникших ошибок (не хешировало пароль)
        user.save()                                                                # - урок 29-если не хешируется пароль именно суперюзера
        return user # - добавил сам

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password', '')) #из словаря данных validated_data выдергиваем пароль с помощью функции pop('password')
                                                                  #пустые кавычки , '')) означают что если пароля нет то что б не вываливалась ошибка
        return super().update(instance, validated_data)

    #после создания сериализатора идем во views.py и передаем данный сериализатор туда для отображения

#-----------------------------------------------------------------------------------------------



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


