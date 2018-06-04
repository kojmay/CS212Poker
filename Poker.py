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
    ranks = ['--23456789TJQKA'.index(str(r)) for r,s in cards]
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
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.
    print iterable
    max_rank = max([card_ranks(item) for item in iterable], key=hand_rank)
    print max_rank
    return [item for item in iterable if card_ranks(item) == max_rank]

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
    # Your code here.
    if numhands*n > len(deck):
        return None
    random.shuffle(deck)
    hands_result = [[deck.pop() for i in range(n)] for j in range(numhands)]
    return hands_result


print deal(5, 5)


# def test():
#     "Test cases for the functions in poker program."
#     sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
#     sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
#     fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
#     fh = "TD TC TH 7C 7D".split() # Full House
#     assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]
#     return 'tests pass'
#
# print test()
