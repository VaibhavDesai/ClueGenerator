from Queue import Queue
from threading import Thread
from pymongo import MongoClient

result = []
class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""

    def __init__(self, tasks):
        client = MongoClient(port=27017)
        self.db = client.business
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            fe = self.tasks.get()
            print id(fe)
            try:
                fe.getNumericValue()

            except Exception, e:
                print e
            finally:
                self.tasks.task_done()


class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, fe):
        """Add a task to the queue"""
        self.tasks.put(fe)


    '''def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))
    '''
    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()

