from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="blog-home"), #
    path('login/', views.login, name='login'), #
    path('logout/', views.logout, name="logout"), #
    path('reset-password', views.resetPass, name='resetPassword'), #
    path('create-new-account', views.register, name='registration'), #
    path('main/', views.main, name='main-site' ), #
    path('main/wirtschaft', views.wiPage, name='wirtschaftsinformatik'), #
    path('main/wirtschaft/mathe', views.moduleMath, name='mathe'), #
    path("<slug:slug>", views.content_detail, name="content_detail"), #
    path("contentList/", views.search_content, name="Content-Liste"), #
    path("addContent/", views.add_content, name="Add Content"), #
    path("aboutUS/", views.aboutUs, name="AboutUs"), #
    path("viewDocuments/", views.search_document, name="ViewDocuments"), #
    path("addDocument/", views.upload_docs, name="UploadDocument"), #
    path("documentDatabase/", views.docDatabase, name="DocumentDatabase"), #
    path("allDocs/", views.ViewAllDocuments.as_view(), name="AllDocs"), #
]
