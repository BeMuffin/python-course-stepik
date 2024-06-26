import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable,list):
    def append(self,element):
        super().append(element)
        self.log(element)
    

logList = LoggableList()
logList.append('msg')