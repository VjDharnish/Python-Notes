import threading
import time
import os
from hdfs import InsecureClient

def read_and_persist_task(hdfs_client, hdfs_directory, db):
    print("Starting task...")
    # Example of reading files from HDFS and persisting data to the DB
    try:
        files = hdfs_client.list(hdfs_directory)
        for file in files:
            file_path = os.path.join(hdfs_directory, file)
            with hdfs_client.read(file_path) as reader:
                data = reader.read()
                # Persist data to the database
                db.persist(data)
        print("Task completed.")
    except Exception as e:
        print(f"Error during task execution: {e}")

def schedule_task(interval, task, *args):
    def wrapper():
        while True:
            start_time = time.time()
            task(*args)
            elapsed_time = time.time() - start_time
            sleep_time = max(0, interval - elapsed_time)
            time.sleep(sleep_time)
    thread = threading.Thread(target=wrapper)
    thread.daemon = True  # Ensure the thread does not block program exit
    thread.start()

# Mock Database class for demonstration
class MockDatabase:
    def persist(self, data):
        print(f"Persisting data: {data[:100]}...")  # Just print the first 100 characters

if __name__ == "__main__":
    hdfs_url = "http://localhost:9870"  # Replace with your HDFS URL
    hdfs_directory = "/path/to/hdfs/directory"
    hdfs_client = InsecureClient(hdfs_url)

    db = MockDatabase()
    interval = 300  # 5 minutes in seconds

    # Schedule the task
    schedule_task(interval, read_and_persist_task, hdfs_client, hdfs_directory, db)

    try:
        while True:
            # Main thread can perform other tasks or just sleep
            time.sleep(1)
    except KeyboardInterrupt:
        print("Scheduler stopped.")
