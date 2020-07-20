import hmm_recursion as hmm
import hmm_true_recursion
import hmmpy as hm
import Markov

if __name__ == '__main__':
    obs = ('happy', 'happy', 'grumpy', 'grumpy', 'grumpy', 'happy', 'happy', 'happy')
    states = ('Sunny', 'Rainy')
    start_p = {'Sunny': 0.667, 'Rainy': 0.333}
    trans_p = {
        'Sunny': {'Sunny': 0.8, 'Rainy': 0.2},
        'Rainy': {'Sunny': 0.4, 'Rainy': 0.6}
    }
    emit_p = {
        'Sunny': {'happy': 0.8, 'grumpy': 0.2},
        'Rainy': {'happy': 0.4, 'grumpy': 0.6}
    }
    print(hmm_true_recursion.calcProb(obs, states, start_p, trans_p, emit_p, todays_latent_state='Rainy'))
    print(hmm_true_recursion.calcProb(obs, states, start_p, trans_p, emit_p, todays_latent_state='Sunny'))

    print(hmm_true_recursion.get_max_path(obs, states, start_p, trans_p, emit_p))
