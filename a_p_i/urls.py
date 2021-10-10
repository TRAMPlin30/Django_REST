from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from a_p_i.views import *

my_api_users = UserViewSet.as_view({'get':'list', 'post':'create'})  #урок 28 -  нужно разрешить запросы на удаление и обновление


# ----------------lesson 18--------------------------
urlpatterns = [
    path('my_notes_list/', My_Notes_List_Mixin.as_view()),
    path('my_notes_list_detail/<int:pk>', My_Notes_Detail_Mixin.as_view()),
    path('my_api_users/', my_api_users, name = 'my_api_users'), #урок 28 - нужно разрешить запросы на удаление и обновлени
]
urlpatterns = format_suffix_patterns(urlpatterns)

#--------------------------------------------------------------------------------------

#------------------------------@api_view(['GET', 'POST'])------------------------------------------------------
#urlpatterns = [
    #path('my_notes_list/', my_notes_list, name='my_notes_list'),
    #path('my_notes_list_detail/<int:pk>', my_notes_list_detail, name='my_notes_list_detail'),
#]
#urlpatterns = format_suffix_patterns(urlpatterns)
#------------------------------@api_view(['GET', 'PUT', 'DELETE'])-----------------------------------------------------
