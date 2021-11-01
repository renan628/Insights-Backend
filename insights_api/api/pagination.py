from rest_framework import pagination

class CardPagination(pagination.LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'limit'
    offset_query_param = 'skip'
    max_limit = 50

    def get_next_link(self):
        if self.offset + self.limit >= self.count:
            return None

        offset = self.offset + self.limit
        return offset

    def get_previous_link(self):
        if self.offset <= 0:
            return None

        offset = self.offset - self.limit
        return offset