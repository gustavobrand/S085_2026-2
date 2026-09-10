import multiprocessing
import zmq, time

def server():
  context = zmq.Context()         
  socket = context.socket(zmq.PUB)          # create a publisher socket
  socket.bind("tcp://*:12346")              # bind socket to the address
  while True:                    
    time.sleep(5)                           # wait every 5 seconds
    t = "GMT " + time.asctime()
    print("Publisher enviando msg: " + t)
    socket.send(t.encode())                 # publish the current time
#-
if __name__ == "__main__": #-
  s = multiprocessing.Process(target=server) #-
#-
  s.start() #-
