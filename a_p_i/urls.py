from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from a_p_i.views import *


# ----------------lesson 18--------------------------
urlpatterns = [
    path('my_notes_list/', My_Notes_List_Mixin.as_view()),
    path('my_notes_list_detail/<int:pk>', My_Notes_Detail_Mixin.as_view()),
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
