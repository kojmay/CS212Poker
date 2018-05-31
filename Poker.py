#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 31/05/2018 22:06
# @Author  : HaifengMay
# @Site    : 
# @File    : Poker.py

# -----------
# User Instructions
#
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    ''' My answer
    card_index = ['--23456789TJQKA'.index(str(r)) for r in ranks]
    for i in range(len(card_index)):
        if i == 0:
            item_val = card_index[0]
        elif item_val == (card_index[i]+1):
            item_val -= 1
        else:
            return False
    return True
    '''
    ### Peter's answer
    return (max(ranks) - min(ranks) == 4) and (len(set(ranks)) == 5)


def flush(hand):
    "Return True if all the cards have the same suit."
    return (len(set([s for r,s in hand])) == 1)


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    ''' My solution
    item_dict = {}
    for item in ranks:
        if item_dict.has_key(item):
            item_dict[item] += 1
        else:
            item_dict[item] = 1
    for key in item_dict.keys():
        if item_dict[key] == n:
            return key
    return None
    '''
    ''' Peter's solution '''
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
        tuple: (highest, lowest); otherwise return None."""
    ''' My Solution
    highest = 0
    lowest = 0
    for r in set(ranks):
        if ranks.count(r) == 2:
            if highest == 0: highest = r
            else: lowest = r
    if lowest != 0:
        return (highest, lowest)
    return None
    '''
    ''' Peter's Solution '''
    hightest = kind(2, ranks)
    lowest = kind(2, list(reversed(ranks)))
    if hightest and hightest != lowest:
        return  (hightest, lowest)
    return None


def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()  # Two pairs
    # assert straight([9, 8, 7, 6, 5]) == True
    # assert straight([9, 8, 8, 6, 5]) == False
    # assert flush(sf) == True
    # assert flush(fk) == False
    # assert card_ranks(sf) == [10, 9, 8, 7, 6]
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    # assert kind(4, fkranks) == 9
    # assert kind(3, fkranks) == None
    # assert kind(2, fkranks) == None
    # assert kind(1, fkranks) == 7
    assert two_pair(tpranks) == (9, 5)
    assert two_pair([9, 9, 8, 5, 2]) == None
    return 'tests pass'


print test()