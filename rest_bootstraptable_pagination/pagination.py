from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from collections import OrderedDict


class BootstrapTablePagination(LimitOffsetPagination):

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('rows', data)
        ]))