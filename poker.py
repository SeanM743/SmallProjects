# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:07:51 2019

@author: snama
"""
import random
import itertools

def poker(hands):
    "Returns a list of winning hands"
    return allmax(hands,key=hand_rank)

def allmax(iterable,key=None):
    "Return a list of all winning hands. Accounts for ties"
    result, maxvals = [],None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxvals:
            result,maxvals = [x],xval
        elif xval == maxvals:
            result.append(x)
    return result

def card_ranks(cards):
    rank_vals = {'A':'14','K':'13','Q':'12','J':'11','T':'10'}
    ranks = [rank_vals.get(r) if r in rank_vals else r for r,s in cards]
    ranks.sort(reverse = True)
    ranks = list(map(int,ranks))
    if ranks == [14,5,4,3,2]:
        return [5,4,3,2,1]
    else:
        return ranks

def straight(ranks):
    return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5

def flush(hand):
    suits = [s for r,s in hand]
    b = [1 if x == suits[0] else 0 for x in suits]
    return all(b)

def kind(n,ranks):
    for k in ranks:
        if ranks.count(k) == n:
            return k
    return None

def two_pair(ranks):
    tp = []
    for p in ranks:
        if ranks.count(p) == 2:
            tp.append(p)
    if len(tp) == 4:
        return tuple(sorted(set(tp),reverse=True))
    else:
        return None

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4,ranks):
        return (7, kind(4,ranks), kind(1,ranks))
    elif kind(3,ranks) and kind(2,ranks):
        return (6,kind(3,ranks),kind(2,ranks))
    elif flush(hand):
        return (5,ranks)
    elif straight(ranks):
        return (4,max(ranks))
    elif kind(3,ranks):
        return (3, kind(3,ranks),ranks)
    elif two_pair(ranks):
        return (2,two_pair(ranks),ranks)
    elif kind(2,ranks):
        return (1, kind(2,ranks),ranks)
    else:
        return (0,ranks)

def test():
    #test cases for functions in poker program        
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()
    
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert two_pair(tpranks) == (9,5)    
    assert kind(4,fkranks) == 9
    assert kind(4,tpranks) == None
    assert straight([9,8,7,6,5]) == True
    assert straight ([9,6,5,4,3]) == False
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk,fh]) == [fk]
    assert poker([fh,fh]) == [fh,fh]
    assert poker([fh]) == [fh]
    assert poker([sf] + 99*[fh]) == [sf]
    assert hand_rank(sf) == (8,10)
    assert hand_rank(fk) == (7,9,7)
    assert hand_rank(fh) == (6,10,7)
    return "tests pass"

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands,n=5,deck=mydeck):
    
    random.shuffle(deck)
    
    return [deck[i*n:i*n+5] for i in range(numhands)]

def best_hand(hand):
    rank, maxval = (0,0,0,0,0),(0,)
    perms = itertools.combinations(hand,5)
    for h in perms:
        rank = hand_rank(list(h))
        if rank > maxval:
            best_hand = list(h)
            maxval = rank
    return best_hand

def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

print(test_best_hand())





        