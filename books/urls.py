from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookModelView.as_view(), name='index'),
    path('books/', views.BookList.as_view(), name='book_list'),
    path('authors/', views.AuthorList.as_view(), name='author_list'),
    path('publishers/', views.PublisherList.as_view(), name='publisher_list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),
]

