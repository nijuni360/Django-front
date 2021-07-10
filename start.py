from waitress import serve
from core.wsgi import application
serve(application, listen='*:8080')