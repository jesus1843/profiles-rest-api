from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Return a list of ApiView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

