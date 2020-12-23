from flask import Flask
from redis import Redis
import os
import logging
host_run=os.environ.get('HOST_RUN', '0.0.0.0')
debug=os.environ.get('DEBUG', 'True')
host_redis=os.environ.get('HOST_REDIS', 'redis')
port_redis=os.environ.get('PORT_REDIS', '6379')
app = Flask(__name__)
redis = Redis(host='redis', port=6379)
@app.route('/')
def hello():
   redis.incr('hits')
   logging.info('escutando a aplicacao')
   print('Mandando a mensagem: ...')
   return 'Hello World! %s times.' % redis.get('hits')
if __name__ == "__main__":
   app.run(host=host_run, debug=True)
