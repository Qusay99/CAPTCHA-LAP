import django
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.http import request, HttpResponseRedirect
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Content, Document
from .forms import CommentForm, ContentForm, NewUserForm, DocumentForm
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.

def home(request):
    return render(request, 'webapp/landingPage.html')

def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('blog-home')

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("main-site")

    form = AuthenticationForm()
    return render(request=request, template_name='webapp/login.html', context={"form":form})

def resetPass(request):
    return render(request, 'webapp/resetPassword.html')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect ("main/")
    form = NewUserForm
    return render(request=request, template_name='webapp/register.html', context={"form":form})

@login_required
def main(request):
    return render(request, 'webapp/main.html')

@login_required
def wiPage(request):
    return render(request, 'webapp/wiPage.html')

def moduleMath(request):
    return render(request, 'webapp/mathe.html')

@login_required
def add_content(request):
    template_name = "webapp/content_add.html"
    new_content = None
    if request.method == "POST":
        content_form = ContentForm(data=request.POST)
        if content_form.is_valid():
            new_content = content_form.save(commit=False)
            new_content.slug = slugify(new_content.header)
            new_content.added_by = request.user
            new_content.save()
        return redirect("main-site")
    else:
        content_form = ContentForm()

    return render(request, template_name, {"content_form": content_form, "new_comment": new_content })

@login_required
def search_content(request):
    if request.method == "POST":
        searched = request.POST.get('searched', False)
        if request.POST["topics"] == "True":
            contents = Content.objects.filter(Q(topic__contains=searched)).exclude(active=False).distinct()
        else:
            contents = Content.objects.filter(Q(header__contains=searched) | Q(description__contains=searched)).exclude(active=False).distinct()
        return render(request, "webapp/content_base.html", {"searched": searched,
                                                            "contents": contents})
    else:
        return render(request, "webapp/content_base.html")

@login_required
def search_content_for_topics(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        contents = Content.objects.filter(Q(topic__contains=searched)).exclude(active=False).distinct()
        return render(request, "webapp/content_base.html", {"searched": searched,
                                                            "contents": contents})
    else:
        return render(request, "webapp/content_base.html")

@login_required
class ContentList(generic.ListView):
    queryset = Content.objects.filter(active=True).order_by("-created_on")
    template_name = "webapp/content_base.html"

@login_required
def content_detail(request, slug):
    template_name = "webapp/content_detail.html"
    content = get_object_or_404(Content, slug=slug)
    comments = content.comments.filter(active=True)
    new_comment = None

    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)

            # Assign the current content to the comment
            new_comment.content = content
            new_comment.author = request.user

            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    return render(request, template_name, { "content": content,
                                            "comments": comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form})


def aboutUs(request):
    return render(request, 'webapp/aboutUs.html')
@login_required
class DocList(generic.ListView):
    queryset = Document.objects.filter(active=True).order_by("-uploaded_on")
    template_name = "webapp/documents.html"

@login_required
def upload_docs(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = Document(docfile = request.FILES['docfile'],  name = form.cleaned_data.get("name"), 
                                                                description = form.cleaned_data.get("description"),
                                                                topic = form.cleaned_data.get("topic"),
                                                                uploader = request.user)
            doc.save()
            return redirect("main-site")
    else:
        form = DocumentForm()

    documents = Document.objects.all()

    return render(request ,"webapp/document_add.html", {'documents': documents, 'form':form})

@login_required
def docDatabase(request):
    return render(request, 'webapp/document_base.html')

@login_required
def search_document(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        documents = Document.objects.filter(Q(name__contains=searched) | Q(description__contains=searched)).exclude(active=False).distinct()
        return render(request, "webapp/documents.html", {"searched": searched,
                                                         "documents": documents})
    else:
        return render(request, "webapp/documents.html")
class ViewAllDocuments(ListView):
    model = Document
    template_name = "webapp/all_documents.html"
    queryset = Document.objects.filter(active=True).order_by("-uploaded_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


