def calcProb(obs : tuple, states : tuple, start_p : dict, trans_p : dict, emit_p: dict, todays_latent_state=None):
    """
    Function to find the path that maximises the probability of resulting in today's latent state.
    Accepts the observations, transition and emission probabilities,
    and returns the most likely hidden states using a hidden Markov model.
    The answer is obtained via a recursive implementation.

    :param obs: The observations in chronological order (obs_t0, ... obs_tn)
    :param states: The set of possible hidden states of the model.
    :param start_p: Starting belief or probability of hidden states at t0
    :param trans_p: Transition probabilities
    :param emit_p: Emission probabilities
    :param todays_latent_state: Today's latent state; latent state at tn
    :return: The probability of the path, and the path of hidden states
    """

    if len(obs) == 1:
        for ob in set(obs):
            if (obs[-1] == ob):
                for state in states:
                    if todays_latent_state == state: #'S':
                        term_thisState = emit_p[state][ob] * start_p[state]
                        return term_thisState, []

    else:
        for ob in set(obs):
            if (obs[-1] == ob):
                for state in states:
                    if todays_latent_state == state:
                        obs_n = obs[:-1]
                        max_prob = 0
                        max_a = []
                        for prev_state in states:
                            a = calcProb(obs_n, states, start_p,trans_p, emit_p, todays_latent_state=prev_state)
                            term_thisState = emit_p[state][ob] * trans_p[prev_state][state] * a[0]
                            # compare and select path that gives maximum probability
                            if term_thisState > max_prob:
                                max_prob = term_thisState
                                previous_state = prev_state
                                max_a = a
                        return max_prob,  max_a[1] + [previous_state]

def get_max_path(obs :  tuple, states : tuple, start_p :  dict, trans_p :  dict, emit_p :  dict):
    """
    Compares the paths leading to the set of hidden states.
    Returns the path resulting to the maximum probability.

    :param obs: The observations in chronological order (obs_t0, ... obs_tn)
    :param states: The hidden states of the model
    :param start_p: Starting belief or probability of hidden states at t0
    :param trans_p: The transition probabilites across hidden states
    :param emit_p: The emission probabilities of the hidden states
    :param todays_latent_state: Today's latent state; latent state at tn
    :return: Most probable hidden path
    """

    max_prob = 0
    max_states = []
    for state in states:
        this_prob, this_states = calcProb(obs, states, start_p, trans_p, emit_p, todays_latent_state=state)
        if this_prob > max_prob :
            max_prob = this_prob
            max_states = this_states + [state]

    return max_states


