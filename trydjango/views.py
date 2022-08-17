"""
Render html web pages
"""
import random
from django.http import HttpResponse




def home_view(request):
    """
    Take in a request
    Return HTML as response
    """

    number = random.randint(1, 50)
    name = "Anton"

    H1_STRING = f"""
    <h1>Hello {name} - {number}</h1>
    """
    P_STRING = f"""
    <p>Hi {name} - {number}</p>
    """
    
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)