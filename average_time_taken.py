import re

object_count_pattern = r"Object Count  :(\d+)"
time_taken_pattern = r"Time Taken:([\d.]+)"
# Object Count  :37424   Time Taken:38.80093002319336
total_time =0 
samples=0
total_objects = 0

log_file_path = "weaviate_insert.log"
with open(log_file_path,"r") as log_file:
    for line in log_file:
        if not line.strip():
            break
        object_count_match = re.search(object_count_pattern, line)
        time_taken_match = re.search(time_taken_pattern, line)

        if object_count_match and time_taken_match:
            object_count = int(object_count_match.group(1))
            total_objects+= object_count
            time_taken = float(time_taken_match.group(1))
            avg_time_per_object = time_taken/object_count
            total_time += avg_time_per_object
            samples+=1

print(f"Total Classes: {samples}")
print(f"Total Objects: {total_objects}")
print(f"Average Time Taken: {total_time/samples}")


