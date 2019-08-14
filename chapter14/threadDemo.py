import threading, time
print('Start of program.')

startTime = time.time()

def takeANap():
    time.sleep(5)
    napTime = time.time()
    print('Wake up! Time elapsed:', round(napTime - startTime, 2))

threadObj = threading.Thread(target=takeANap)
threadObj.start()

endTime = time.time()
print('End of program. Time elapsed:', round(endTime - startTime, 2))