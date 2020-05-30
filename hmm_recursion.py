import numpy as np
import math


def calcProb(obs, todays_latent_state=None):
    # 1=happy
    # 0=grumpy
    # obs = [H,G,G,G,H...] == [1,0,0,0,1....]
    # n: length of obs/ number of obs/days we have

    count = 0

    # Emission probabilities
    pHS = 0.8
    pGS = 1 - pHS
    pHR = 0.4
    pGR = 1 - pHR

    # Transition probabilities
    pSS = 0.8
    pSR = 0.4
    pRR = 0.6
    pRS = 0.2
    pS = 2 / 3
    pR = 1 / 3

    if len(obs) == 1:
        if (obs[-1] == 1):  # this state is happy
            if todays_latent_state == 'S':
                termS = pHS*pS
                return termS, []
            if todays_latent_state == 'R':
                termR = pHR * pR
                return termR, []
        if (obs[-1] == 0):  # this state is grumpy
            if todays_latent_state == 'S':
                termS = pGS * pS
                return termS, []
            if todays_latent_state == 'R':
                termR = pGR * pR
                return termR, []



    if (obs[-1] == 1):  # this state is happy
        if todays_latent_state == 'S':
            obs_n = obs[:-1]
            # previous day is sunny
            a = calcProb(obs_n, todays_latent_state='S')
            termS = pHS * pSS * a[0]
            #  previous is rainy
            b = calcProb(obs_n, todays_latent_state='R')
            termR = pHS * pSR * b[0]
            # compare and select path that gives maximum probability
            if termS > termR:
                return termS,  a[1] + ['S']
            else:
                return termR, b[1] + ['R']
        if todays_latent_state == 'R':
            obs_n = obs[:-1]
            # previous day is sunny
            a = calcProb(obs_n, todays_latent_state='S')
            termS = pHR * pRS * a[0]
            #  previous dat is rainy
            b = calcProb(obs_n, todays_latent_state='R')
            termR = pHR * pRR * b[0]
            if termS > termR:
                return termS, a[1] + ['S']
            else:
                return termR, b[1] + ['R']
    if (obs[-1] == 0):  # this state n is grumpy
        if todays_latent_state == 'S':
            obs_n = obs[:-1]
            # previous day was sunny
            a = calcProb(obs_n, todays_latent_state='S')
            termS = pGS * pSS * a[0]
            #  previous day was rainy
            b = calcProb(obs_n, todays_latent_state='R')
            termR = pGS * pSR * b[0]
            if termS > termR:
                return termS, a[1] + ['S']
            else:
                return termR, b[1] + ['R']
        if todays_latent_state == 'R':
            obs_n = obs[:-1]
            # previous day was sunny
            a = calcProb(obs_n, todays_latent_state='S')
            termS = pGR * pRS * a[0]
            #  previous day was rainy
            b = calcProb(obs_n, todays_latent_state='R')
            termR = pGR * pRR * b[0]
            if termS > termR:
                return termS, a[1] + ['S']
            else:
                return termR, b[1] + ['R']


