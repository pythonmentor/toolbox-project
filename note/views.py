from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Note
from.forms import NoteForm

# from django.core.paginator import Paginator

class ViewNote(ListView):
    model = Note
    template_name = 'note/note.html'
    paginate_by = 6
    
    # # ordering = ['-id']

class AddNoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note/add_note.html"
    
    
class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/detail_note.html'
    

class ModifNoteView(UpdateView):
    model = Note
    template_name = "note/modif_note.html"
    form_class = NoteForm
    
    
class DeleteNote(DeleteView):
    model = Note
    template_name = 'note/delete_note.html'
    success_url = reverse_lazy('note')