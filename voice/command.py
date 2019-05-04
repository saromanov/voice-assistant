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