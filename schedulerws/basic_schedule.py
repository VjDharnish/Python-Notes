import schedule
import time
import threading
import multiprocessing


# Function to be scheduled
def job():
    print(threading.currentThread().getName())
    print("I'm a scheduled job.")
    time.sleep(20)

    print("My job  is done")

# Schedule the job
def schedule_job():
    print(f"scheduled jobs: 1")
    i =10
    while i!=0:
        schedule.every(10).seconds.do(job)
        i-=1
    while True:
        try:
            schedule.run_pending()
        except KeyboardInterrupt:
            count = len(schedule.jobs)
            print(f"Number of scheduled jobs: {count}")
            break



if __name__ =='__main__':
    # Get the count of scheduled jobs
    t1 = multiprocessing.Process(target=schedule_job)
    t1.start()
    t1.join()
    

