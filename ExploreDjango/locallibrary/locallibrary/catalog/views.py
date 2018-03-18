from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    num_generes = Genre.objects.count()
    num_authours_choudhary = Author.objects.filter(last_name__contains='choudhary')

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
                 'num_generes':num_generes,'num_authours_choudhary':num_authours_choudhary
                },
    )

def allbooks(request):
    return render(
        request,
        'all boooks willb e here shortly'
    )

from django.views import generic

class BookListView(generic.ListView):
    model = Book # it s really just shorthand for saying queryset = Book.objects.all()
    # context_object_name = 'list_of_books'

    paginate_by = 5

    def get_queryset(self):
        # return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book
    """
    if we don't want to use above BookDetailView then we can write it as below
    how you would implement the class-based view as a function, if you were not using the generic class-based detail view.

    def book_detail_view(request,pk):
        try:
            book_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

        #book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/book_detail.html',
            context={'book':book_id,}
        )
    """

class AuthorListView(generic.ListView):
    model = Author # it s really just shorthand for saying queryset = Book.objects.all()
    
    paginate_by = 4

    def get_queryset(self):
        # return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
        return Author.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data about authors'
        return context

class AuthorDetailView(generic.DetailView):
    model = Author
