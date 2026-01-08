from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class BookPagePagination(PageNumberPagination):
    page_size = 1
    max_page_size = 10
    
class BookOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 20
    
class BookCursorPagination(CursorPagination):
    page_size = 5
    ordering = ("-id")