import hmm_recursion as hmm
import hmmpy as hm
import Markov

if __name__ == '__main__':
    print(hmm.calcProb([1,1,0,0,0,1], 'S'))
    print(hmm.calcProb([1,1,0,0,0,1], 'R'))


