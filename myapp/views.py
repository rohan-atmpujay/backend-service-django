from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Book
from .serializers import BookSerializer
from .pagination import BookPagePagination, BookOffsetPagination, BookCursorPagination
# Create your views here.


# Example of CRUD using APIViews

# List and Create Book using APIView
# class BookListCreateAPIView(APIView):
    
#     def get(self):
#         book = Book.objects.all()
#         serializer = BookSerializer(book, many=True)
#         return Response(serializer.data)    
    
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)   
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    
    
# Retrive, Update and Delete Book using APIView
# class BookDetailAPIView(APIView):
    
#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return None
        
#     # Retrive one
#     def get(self, request, pk):
#         book = self.get_object(pk=pk)
#         if not book:
#             return Response({"error": 'Book not found'},
#                             status=status.HTTP_404_NOT_FOUND
#                             )
            
#         serializer = BookSerializer(book)
#         return Response(serializer.data)

#     # Update
#     def put(self, request, pk):
#         book = self.get_object(pk=pk)
#         if not book:
#             return Response({"error": 'Book not found'},
#                             status=status.HTTP_404_NOT_FOUND
#                             )
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # Delete
#     def delete(self, request, pk):
#         book = self.get_object(pk=pk)
#         if not book:
#             return Response({"error": 'Book not found'},
#                             status=status.HTTP_404_NOT_FOUND
#                             )
            
#         book.delete()
#         return Response(
#             {"message": "Book deleted"},
#             status=status.HTTP_204_NO_CONTENT
#             )



# Example of CRUD using GenericViews

# class BookListCreateAPIView(generics.ListCreateAPIView):
#     '''
#     API for creating and listing book using ListcreateAPIView(Concrete API view)
#     '''
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
#     # override 
#     def list(self, request, *args, **kwargs):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)

# class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# Example of CRUD using ViewSets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.order_by('pk')
    serializer_class = BookSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = BookCursorPagination
    
    
    # Custom action 
    @action(detail=False, methods=["get"])
    def popular(self, request):
        return Response({"message": "Popular books"})