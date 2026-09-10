import multiprocessing #-
import zmq
from time import sleep #-

def server():
  context = zmq.Context()
  socket  = context.socket(zmq.ROUTER)    
  socket.bind("tcp://*:12345")            
  print("Servidor inicializado na porta 12345")

  while True:
    print("Servidor pronto para receber msgs com ROUTER")
    ident, message = socket.recv_multipart()
    if not "STOP" in str(message):        
      print("Servidor recebeu uma msg: " + str(message.decode()))
      reply = str(message.decode())+'*'   
      print("Servidor enviando uma resposta: " + reply +  " para " + str(ident))
      socket.send_multipart([ident, reply.encode()])
    else:
      print("Servidor recebeu um STOP... finalizando")
      break                               

def client():
  context = zmq.Context()
  socket  = context.socket(zmq.DEALER)
  ident = u'worker-01'
  socket.identity = ident.encode('ascii')

  socket.connect("tcp://localhost:12345") 
  print("Cliente conectado na porta 12345 com DEALER")
  socket.send(b"Hello world")             
  print("Cliente " + str(ident) + " enviou mensagem de Hello World")
  message = socket.recv()                 
  print("Cliente recebeu resposta: " + str(message.decode()))
  # socket.send(b"STOP")                    
  # print("Cliente enviou STOP")

def client2():
  context = zmq.Context()
  socket  = context.socket(zmq.DEALER)
  ident = u'worker-02'
  socket.identity = ident.encode('ascii')

  socket.connect("tcp://localhost:12345") 
  print("Cliente conectado na porta 12345 com DEALER")
  socket.send(b"Hello world")             
  print("Cliente " + str(ident) + " enviou mensagem de Hello World")
  message = socket.recv()                 
  print("Cliente recebeu resposta: " + str(message.decode()))
  # socket.send(b"STOP")                    
  # print("Cliente enviou STOP")

def client3():
  context = zmq.Context()
  socket  = context.socket(zmq.DEALER)
  ident = u'worker-03'
  socket.identity = ident.encode('ascii')

  socket.connect("tcp://localhost:12345") 
  print("Cliente conectado na porta 12345 com DEALER")
  socket.send(b"Hello world")             
  print("Cliente " + str(ident) + " enviou mensagem de Hello World")
  message = socket.recv()                 
  print("Cliente recebeu resposta: " + str(message.decode()))
  socket.send(b"STOP")                    
  print("Cliente enviou STOP")

#-
if __name__ == "__main__": #-
  s = multiprocessing.Process(target=server) #-
  c = multiprocessing.Process(target=client) #-
  c2 = multiprocessing.Process(target=client2) #-
  c3 = multiprocessing.Process(target=client3) #-
#-
  s.start() #-
  sleep(2) #-
  c.start() #-
  c2.start() #-
  c3.start() #-
  c.join() #-
  c2.join() #-
  c3.join() #-
  s.join() #-
