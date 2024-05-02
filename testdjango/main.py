import time
import multiprocessing

def mySleep(t):
    print(f"Sleeping for {t}")
    time.sleep(t)

def main():
    times= [2,3,4,5,2,2,2,4,4,3]
    pool = multiprocessing.Pool(4)
    pool.map(mySleep,times)


if __name__ == "__main__":
    main()