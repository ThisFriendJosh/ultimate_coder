import time

def time_function(fn, *args, **kwargs):
    start = time.time()
    fn(*args, **kwargs)
    return time.time() - start

def main():
    duration = time_function(lambda: sum(range(1000)))
    print(f"Duration: {duration:.6f}s")

if __name__ == "__main__":
    main()
