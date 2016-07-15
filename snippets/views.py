from rest_framework import mixins
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

"""
Mixins : View classes built on GenericAPIView
"""

class SnippetList(generics.ListCreateAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

