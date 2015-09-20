import bottle
from bottle import run, route, request
import os

@route('/')
def index():
   return "Ziju !"

@route('/pozdrav')
def pozdrav():
   osloveni = os.getenv('OSLOVENI', 'Ahoj')
   jmeno = request.query.jmeno
   output = '<center><h1>%s %s !</h1></center>'
   return output % (osloveni, jmeno)

run(host='0.0.0.0', port=os.getenv('PORT', 8080))
