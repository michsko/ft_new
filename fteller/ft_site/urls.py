from django.urls import path
from  .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"), 
    path('work', views.work, name="work"),
    path('foto', views.foto, name="foto"),
    path('kontakt', views.kontakt, name="kontakt"),
    path('standup', views.standup, name="standup"),
    path('moderation', views.moderation, name="moderation"),
    path('film', views.film, name="film"),
    path('divadlo',views.divadlo, name="divadlo"),
    path('program',views.program, name="program"),
    path('event_add', views.program_add, name='event_add'),
    path('add_event', views.add_event, name="add_event"),
    path('event_update/<event_id>', views.event_update, name='event_update'),
    path('event_delete/<event_id>', views.event_delete, name='event_delete'),
]
