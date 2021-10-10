from rest_framework.decorators import api_view


from my_notes.models import MyNotes
from a_p_i.serializers import NoteSerializer #ThinNoteSerializer # ThinNoteSerializer - если нужно отобразить не все а только нужные поля
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # урок 26 (права доступа) без авторизации невозможно постить и смотреть - http://127.0.0.1:8000/api/my_notes_list/ - будет надпись "detail": "Authentication credentials were not provided."

# ----------------lesson 20,21-------на основе миксинов-------------------

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView


class My_Notes_List_Mixin(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = MyNotes.objects.all()
    serializer_class = NoteSerializer
# в уроке 27 расказано об правах подробно - являешся автором записи - можешь удалить если ты не автор - то удалять запись нет прав.
    permission_classes = (IsAuthenticated,) # урок 26 (права доступа) без авторизации невозможно постить и смотреть - http://127.0.0.1:8000/api/my_notes_list/  - будет надпись "detail": "Authentication credentials were not provided."
                                            # insomnia тоже покажет "detail": "Invalid username/password."
    def get(self, request, *args, **kwargs):
        self.serializer_class = NoteSerializer
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer): # видео 24
        serializer.save(author=self.request.user) #обращаемся к записи в самом запросе к серверу
        #в request прописан авторизованный user, который обращается к серверу по умолчанию прописанный в в request


class My_Notes_Detail_Mixin(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = MyNotes.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ---------------урок 28---------------------делаем сериалайзер для возможности добавления юзеров по API-------------
from a_p_i.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet, ViewSetMixin
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser

class UserViewSet(ModelViewSet):
    model = get_user_model()  # функция которая возвращает модель текущего юзера
    queryset = model.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
#после создания данного класса отображения переходим в a_p_i/urls.py и прописываем адрес для перехода к данному API
# -----------------------------------------------------------------------------------------------------------------


#---------------lesson 18--- -----------------------
'''
from rest_framework.views import APIView



class My_Notes_List(APIView):
    def get(self, request, format=None):
        notes = MyNotes.objects.all()
        #context = {'request':request} - иногда бывает необходимость в использовании внутри сериалайзера request - то его нужно передавать в переменной context
        serializer = NoteSerializer(notes, many=True) #- ...many=True, context=context) -такая необходимость (как лайфхак) при использовании в url = HyperlinkedIdentityField(view_name='notes-detail')
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class My_Notes_List_Detail(APIView):
    def get_object(self, pk):
        try:
            note = MyNotes.objects.get(pk=pk)
            return note
        except MyNotes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)  # ThinNoteSerializer(serializer.py) - для отображения только выбранных полей
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)  # ThinNoteSerializer(serializer.py) - для отображения только выбранных полей
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

# --------------------------------------------------------------------------------

#@api_view(['GET', 'POST'])
#def my_notes_list(request, format=None):
    #if request.method == 'GET':
        #notes = MyNotes.objects.all()
        #serializer = NoteSerializer(notes, many=True)
        #return Response(serializer.data)
    #elif request.method == 'POST':
        #serializer = NoteSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#@api_view(['GET', 'PUT', 'DELETE'])
#def my_notes_list_detail(request, pk, format=None):
    #try:
        #note = MyNotes.objects.get(pk=pk)
        #except MyNotes.DoesNotExist:
        #return Response(status=status.HTTP_404_NOT_FOUND)
    #if request.method == 'GET':
        #serializer = NoteSerializer(note)
        #return Response(serializer.data)
        #elif request.method == 'PUT':
        #serializer = NoteSerializer(note, data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #elif request.method == 'DELETE':
        #note.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)

#---------------------------------------------------------------------------------------------------------