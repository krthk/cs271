'''
Created on Dec 3, 2014
@author: Karthik Puthraya
'''

class Ballot():
    '''
    This is the ballot number for a given node
    '''

    def __init__(self, ip, port, n = 0):
        '''
        Initiate the ballot with the IP address
        '''
        def __ip_to_int(ip, port):
            nums = map(int, ip.split('.'))
            total = 0
            for i in range(4):
                total += nums[-i-1]*(256**i)
            return total*100000 + port
        
        self.n = n
        self.nodeIdentifier = __ip_to_int(ip, port)
        
    def increment(self):
        self.n += 1
    
    def set_n(self, n):
        self.n = n

    def __lt__(self, other):
        if self.n < other.n : 
            return True
        elif self.n == other.n: 
            return self.nodeIdentifier < other.nodeIdentifier
        else: 
            return False

    def __le__(self, other):
        if self.n < other.n : 
            return True
        elif self.n == other.n: 
            return self.nodeIdentifier <= other.nodeIdentifier
        else: 
            return False

    def __eq__(self, other):
        if not isinstance(other, Ballot):
            return False
        return self.n == other.n and self.nodeIdentifier == other.nodeIdentifier

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self.n > other.n : 
            return True
        elif self.n == other.n: 
            return self.nodeIdentifier > other.nodeIdentifier
        else: 
            return False
    
    def __ge__(self, other):
        if self.n > other.n : 
            return True
        elif self.n == other.n: 
            return self.nodeIdentifier >= other.nodeIdentifier
        else: 
            return False    
            
    def __str__(self):
        return '<{0}, {1}>'.format(self.n, self.nodeIdentifier)
        
if __name__ == '__main__':
    b = Ballot('127.0.0.1', 5555)
    print b
    b3 = Ballot('127.0.0.1', 5557)
    print b3
    b2 = Ballot('169.231.142.95', 5555)
    print b.n, b.nodeIdentifier
    print b < b3 
    b.increment()
    print b
    print b < b3
    print b <> b3
    print b2 > b3