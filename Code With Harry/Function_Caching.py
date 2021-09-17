# What is the term caching means?
# Caching means to store the data in a place from where it can be served faster. In case of data that has been frequently used, the computer assigns a cache memory, so it does not have to load it again and again from the main memory. The purpose of the cache is to make the tasks more efficient and quicker. The same is true for web browsers, the pages we load again and again are stored in the cache for faster retrieval. In Python, however, we have to do it all manually, as the program will not store anything in the cache itself.


import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Done... Calling again")
    input()
    some_work(3)
    print("Called again")


#Notes
# This Function will not call line22 because it has been cached, First call was some_word(3) in line 16 as we have set maxsize=3 so it will stor 3 recent calls in it therfore some_work(3) will be cached.