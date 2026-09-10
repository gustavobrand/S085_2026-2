import multiprocessing
import zmq, time

def client():
  context = zmq.Context()
  socket = context.socket(zmq.SUB)          # create a subscriber socket
  socket.connect("tcp://localhost:12345")   # connect to the server
  socket.setsockopt(zmq.SUBSCRIBE, b"TIME") # subscribe to TIME messages

  for i in range(5):      # Five iterations
    time = socket.recv()  # receive a message related to subscription 
    print("Subscriber recebendo msg: " + time.decode())  # print the result      
#-
if __name__ == "__main__": #-
  c = multiprocessing.Process(target=client) #-
#-
  c.start() #-
  c.join() #-
