from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register, login_user, logout_user
from main.views import plus, minus, remove
from main.views import get_item_json, create_ajax, plus_ajax, minus_ajax, remove_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('plus/<int:id>/', plus, name='plus'),
    path('minus/<int:id>/', minus, name='minus'),
    path('remove/<int:id>/', remove, name='remove'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('plus-ajax/', plus_ajax, name='plus_ajax'),
    path('minus-ajax/', minus_ajax, name='minus_ajax'),
    path('remove-ajax/', remove_ajax, name='remove_ajax'),
]