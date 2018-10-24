import sys
import itertools

def get_pf(T):
    products = itertools.product(T, T)
    return not any(x.startswith(y) for x, y in products if x != y)


def remove_prefix(prefix, S):
    ''' Remove prefix from S.'''
    return S[len(prefix):]

def find_prefix(prefix, L):
    ''' Return the dangling suffixes of each matching string.'''
    dangling = []
    for l in L:
        if l.startswith(prefix):
            dangling.append(remove_prefix(prefix, l))
    return set(dangling)

def cross_prefix(L1, L2):
    ''' Return the dangling suffixes between 2 lists. '''
    L1L2 = set()
    for l1 in L1:
        L1L2 |= find_prefix(l1, L2)

    L2L1 = set()
    for l2 in L2:
        L2L1 |= find_prefix(l2, L1)
    return L1L2 | L2L1

def unique_decode(codewords):
    # Only for the first iteration.
    # Find the dangling suffixes between the first 
    # set and the codeword.
    C = {}
    C[0] = set()
    for c in codewords:
        C[0] |= find_prefix(c, codewords - set([c]))                
    
    i = 1
    while True:
        C[i] = cross_prefix(C[i-1],codewords)
        #print i, C[i] # print each set if you wish.
        if '' in C[i]:
            return False
        
        # Check if C[i] is equal with any other previous set.
        # If yes, the code is uniquely decodable.
        for j in range(0,i):
            if C[j] == C[i]:
                return True
        i = i + 1

if __name__ == "__main__":
    T = sys.argv[1].split(',')
    print('Prefix-Free: ', get_pf(T))
    print('Uniquely Decomposable: ', unique_decode(set(T)))
