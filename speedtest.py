from alkobeast import parameterAtIndex, thresholdApplyer, allItems
import time

start_time = None

def startTimer():
    global start_time
    start_time = time.time()

def stopTimer():
    global start_time
    if start_time is None:
        raise ValueError("Timer has not been started")
    elapsed_time = time.time() - start_time
    start_time = None
    return elapsed_time

def test():
    x = allItems()
    for apk in range(0,300,10):
        for alcoholPrecentage in range(0,100,10):
            for volume in range(0,1000,10):
                for price in range(0,1000,10):
                    y = len(thresholdApplyer(x, alcoholPrecentage, 100, apk, 300, volume, 1000, price, 1000))
                    print(y)
                    if (y == 0):
                        return

startTimer()

test()

print(stopTimer(), "seconds")
