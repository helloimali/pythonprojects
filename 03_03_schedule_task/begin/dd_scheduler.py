import threading
import schedule
import time

# threading.Thread allows us to make it multi threaded
class DailyDigestScheduler(threading.Thread):
    def __init__(self):
        # call the inheritewd class init
        super().__init__()
        self.__stop_running = threading.Event()
    
    def scedule_daily(self, hour, min, job):
        schedule.clear()
        schedule.every().day.at(f'{hour:02d}:{min:02d}').do(job)
        
    def run(self):
        self.__stop_running.clear()
        while not self.__stop_running.is_set():
            schedule.run_pending()
            time.sleep(1)

    def stop(self):
        self.__stop_running.set()
    

if __name__ == "__main__":
    import dd_email
    email = dd_email.DailyDigestEmail()

    sced = DailyDigestScheduler()
    sced.start()

    hour = time.localtime().tm_hour
    min = time.localtime().tm_min + 1
    sced.scedule_daily(hour,min,email.send_email)

    time.sleep(60)
    sced.stop()
