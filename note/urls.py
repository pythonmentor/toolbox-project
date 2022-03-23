from django.urls import path

from .views import NoteDetailView, ViewNote, AddNoteView, ModifNoteView, DeleteNote


urlpatterns = [
    path('', ViewNote.as_view(), name = 'note'),
    path('detail_note/<int:pk>', NoteDetailView.as_view(), name = 'detail_note'),
    path('add_note/', AddNoteView.as_view(), name = 'add_note'),
    path('detail_note/edit/<int:pk>', ModifNoteView.as_view(), name = 'modif_note'),
    path('remove/<int:pk>', DeleteNote.as_view(), name = 'delete_note'),
    ]