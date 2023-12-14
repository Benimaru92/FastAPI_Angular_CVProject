from tqdm import tqdm
import time

# Create a list of items to iterate over
items = list(range(10))

# Wrap the iterable with tqdm to create a progress bar
for item in tqdm(items, desc="Processing items", unit="item"):
    # Simulate a time-consuming task
    time.sleep(0.1)