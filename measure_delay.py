import time
import requests

def measure_avg_response_time(url, repetitions=10, method='GET', **kwargs):
    total_time = 0
    for _ in range(repetitions):
        start_time = time.time()
        
        if method.upper() == 'GET':
            response = requests.get(url, **kwargs)
        elif method.upper() == 'POST':
            response = requests.post(url, **kwargs)
        elif method.upper() == 'PUT':
            response = requests.put(url, **kwargs)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, **kwargs)
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        end_time = time.time()
        total_time += (end_time - start_time)
        
        # Ensure the request was successful (optional)
        response.raise_for_status()
    
    avg_response_time = total_time / repetitions
    return avg_response_time

# Example usage
url = "https://weaviate.kites.localzoho.com"
avg_time = measure_avg_response_time(url, repetitions=20)
print(f"Average API response time: {avg_time:.5f} seconds")
