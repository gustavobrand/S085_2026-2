import multiprocessing
import zmq, time

def client():
  context = zmq.Context()
  socket = context.socket(zmq.SUB)          # create a subscriber socket
  socket2 = context.socket(zmq.SUB)          # create a subscriber socket
  socket.connect("tcp://localhost:12345")   # connect to the server
  socket2.connect("tcp://localhost:12346")   # connect to the server
  socket.setsockopt(zmq.SUBSCRIBE, b"TIME") # subscribe to TIME messages
  socket2.setsockopt(zmq.SUBSCRIBE, b"GMT") # subscribe to GMT messages

  for i in range(5):      # Five iterations
    time = socket.recv()  # receive a message related to subscription 
    print("Subscriber recebendo msg: " + time.decode())  # print the result      
    time2 = socket2.recv()  # receive a message related to subscription 
    print("Subscriber recebendo msg: " + time2.decode())  # print the result      
#-
if __name__ == "__main__": #-
  c = multiprocessing.Process(target=client) #-
#-
  c.start() #-
  c.join() #-
