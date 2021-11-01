from rest_framework import pagination

class CardPagination(pagination.LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'limit'
    offset_query_param = 'skip'
    max_limit = 50