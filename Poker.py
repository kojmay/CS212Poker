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

import random # this will be a useful library for shuffling

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
    # print 'card_ranks: ', cards
    # print "cards:", cards
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

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    # retList = allmax(hands, key=hand_rank)
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.
    # print iterable
    max_rank = max([item for item in iterable], key=hand_rank)
    # print "max_rank:",max_rank
    return [item for item in iterable if card_ranks(item) == card_ranks(max_rank)]


def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    # Your code here.
    if numhands*n > len(deck):
        return None
    random.shuffle(deck)
    hands_result = [deck[i*n: (i+1)*n] for i in range(numhands)]
    return hands_result

hand_names = ["Straight Flush", "4 Kind", "Full house", "Flush", "Straight", "3 kind", "2 pairs", "1 pair", "High card"]

def hand_percentages(n = 700*1000):
    counts= [0] * 9
    for i in range(n/10):
        for hand in deal(10):
            rank = hand_rank(hand)[0]
            counts[rank] += 1
    for i in reversed(range(9)):
        print "%14s: %6.3f %%" % (hand_names[i], 100*counts[i]/n)



# Problem Set 1: Seven Card Stu
import itertools

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    ''' My solution
    all_hands =[list(item) for item in itertools.combinations(hand, 5)]
    max_rank = max([item for item in all_hands], key=hand_rank)
    result = [item for item in all_hands if card_ranks(item) == card_ranks(max_rank)]
    if len(result) == 1:
        return result[0]
    else:
        return result
    '''
    ''' Peter's solution'''
    return max(itertools.combinations(hand, 5), key=hand_rank)


def test_best_hand():
    print (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split())))
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

# print test_best_hand()

allranks = "23456789TJQK"
redcards = [r+s for r in allranks for s in 'DH']
blackcards = [r+s for r in allranks for s in 'SC']

def replacements(card):
    if card == '?B':
        return blackcards
    elif card == '?R':
        return redcards
    else:
        return [card]

def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    # print hand
    print map(replacements, hand)
    print [item for item in itertools.product(*map(replacements, hand))]

    hands = set(best_hand(h) for h in itertools.product(*map(replacements, hand)))
    return max(hands, key=hand_rank)


    # Your code here

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    # assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
    #         == ['7C', 'TC', 'TD', 'TH', 'TS'])
    # assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
    #         == ['7C', '7D', '7H', '7S', 'JD'])
    # return 'test_best_wild_hand passes'

print test_best_wild_hand()