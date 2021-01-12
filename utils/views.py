from django.shortcuts import render

class EnablePartialUpdateMixin:

    def update(self, request, *args, **kwargs):
        self.kwargs['partial'] = True
        return super().update(request, *args, **kwargs)