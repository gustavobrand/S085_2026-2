import multiprocessing #-
import zmq
from time import sleep #-

def server():
  context = zmq.Context()
  socket  = context.socket(zmq.REP)       # create reply socket
  socket.bind("tcp://*:12345")            # bind socket to address
  print("Servidor inicializado na porta 12345")

  while True:
    print("Servidor pronto para receber msgs")
    message = socket.recv()               # wait for incoming message
    if not "STOP" in str(message):
      reply = str(message.decode())+'*'   # append "*" to message
      socket.send(reply.encode())         # send it away (encoded)
    else:
      print("Servidor recebeu um STOP... finalizando")
      break                               # break out of loop and end

def client():
  context = zmq.Context()
  socket  = context.socket(zmq.REQ)       # create request socket

  socket.connect("tcp://localhost:12345") # block until connected
  print("Cliente conectado na porta 12345")
  socket.send(b"Hello world")             # send message
  print("Cliente enviou mensagem de Hello World")
  message = socket.recv()                 # block until response
  print("Cliente recebeu resposta: " + str(message.decode()))
  socket.send(b"STOP")                    # tell server to stop
  print("Cliente enviou STOP")
  #print(message.decode())                 # print result
#-
if __name__ == "__main__": #-
  s = multiprocessing.Process(target=server) #-
  c = multiprocessing.Process(target=client) #-
#-
  s.start() #-
  sleep(2) #-
  c.start() #-
  c.join() #-
  s.join() #-
