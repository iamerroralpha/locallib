from django.shortcuts import render

# Create your views here.


#first we will import the models we already defined


from .models import Book, Author, BookInstance, Genre, Language
# we define the index function that will be called in the urls.py that is called index
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
    num_lang = Language.objects.count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context=
        		{
        		'num_books':num_books,
        		'num_instances':num_instances,
        		'num_instances_available':num_instances_available,
        		'num_authors':num_authors,
        		'num_lang':num_lang
        		},
    )

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
