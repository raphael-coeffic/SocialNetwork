class Observer:
    def update(self, message):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        if observer not in self.observers:  # add to observer only if he is not an observer in the present
            self.observers.append(observer)

    def detach(self, observer):
        try:
            self.observers.remove(observer)   # detach someone from the list of the observers
        except ValueError:
            pass

    def notify_observers(self, message):    # send notifications to all the observers of this user
        for observer in self.observers:
            observer.update(message)


