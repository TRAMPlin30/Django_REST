from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from a_p_i.views import *

urlpatterns = [
    path('my_notes_list/', my_notes_list, name='my_notes_list'),
    path('my_notes_list_detail/<int:pk>', my_notes_list_detail, name='my_notes_list_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

