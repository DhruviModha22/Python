import time

def example_function():
    time.sleep(2)  # Simulating a time-consuming task

start_time = time.time()
example_function()
end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.2f} seconds")