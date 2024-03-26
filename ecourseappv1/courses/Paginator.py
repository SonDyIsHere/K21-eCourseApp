from rest_framework import pagination


class CoursesPaginator(pagination.PageNumberPagination):
    page_size = 1