import datetime as d
import time as t

star_t = t.time()
end_t = star_t + 5
while t.time() < end_t:
    print(d.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    t.sleep(1)
