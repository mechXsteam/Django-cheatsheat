from django.urls import path

from . import views

app_name = 'my_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topic'),
    path('entries/<int:topic_id>', views.entry, name='entry'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    path('delete_topic/<int:topic_id>', views.delete_topic, name='delete_topic'),
    path('delete_entry/<int:entry_id>', views.delete_entry, name='delete_entry', )
]
