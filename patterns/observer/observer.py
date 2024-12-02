from abc import ABC, abstractmethod
import threading

class Subject():

    observers = []
    
    def attach(self, observer):
        self.observers.append()

    def detach(self, observer):
        self.observers.remove()

    def notify(self):
        data = self.observers

        if len(data)>0:

            threads = []
            for i in range(len(data)):
                thread = threading.Thread(target=data[i].update,args=(self,))
                threads.append(thread)

            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join()
                pass

class Observer():

    def update(self, subject):
        pass