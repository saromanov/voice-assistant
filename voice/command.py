import datetime

class Command:
    '''
    Command defines base class for any command
    '''
    def __init__(self):
        pass
    
    def recv(self):
        raise NotImplementedError
    
    def response(self):
        raise NotImplementedError


class Time(Command):
    ''' represents time command for voice 
    '''
    def __init__(self):
        super().__init__()
    
    def recv(self):
        return
    
    def response(self):
        now = datetime.datetime.now()
        return 'Current time is {0} hours {1} minutes'.format(now.hour, now.minute)
