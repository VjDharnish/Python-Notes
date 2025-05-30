import signal
import time

def receive_signal(signum, stack):
    # print(f"Process running with PID {os.getpid()}")
    print(f"Received signal {signum}")
    if signum == signal.SIGINT:
        print("SIGINT received, shutting down gracefully...")
        exit(0)
    elif signum == signal.SIGTERM:
        print("SIGTERM received, shutting down gracefully...")
        exit(0)

signal.signal(signal.SIGTERM, receive_signal) # use kill command to trigger SIGTERM 
#use keyboard interrupt to trigger SIGINT

# print(f"Process running with PID {os.getpid()}")
try:
    while True:
        print("Application is running")
        time.sleep(5)
except KeyboardInterrupt:
    print("KeyboardInterrupt received, shutting down gracefully...")
        