import datetime
import time

epochtime = 30256871
currentEpochTime = time.time()
datetime = datetime.datetime.fromtimestamp(epochtime + currentEpochTime)

print(datetime)
