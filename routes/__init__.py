from flask import Blueprint

# Blueprint para as rotas
bp = Blueprint('routes', __name__)

# Importar rotas de outros arquivos
from .usuarios import *
from .index import *