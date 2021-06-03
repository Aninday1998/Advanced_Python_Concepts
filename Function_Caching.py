# Function Caching

import time
from functools import lru_cache

@lru_cache(maxsize = 11)
def somework(n):
    # some task is taking n seconds
    time.sleep(5)
    return n

print("Now running somework().")
somework(5)
somework(1)
somework(2)
somework(3)
print("Done Calling. Calling again somework().")
somework(5)
print("Called Again")



