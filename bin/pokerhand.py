# !/usr/bin/python3
# -*- encoding: utf-8 -*-

'''
Created on 27 de set de 2021
@module: bin.pokerhand
@summary:
@author: Sandro Regis Cardoso | Software Engineer
@contact: src.softwareengineer@gmail.com
'''

import random


class PokerHand(object):
    '''
    classdocs
    @todo: Produce the full documentation for this class
            Implement the methods on unittest here
    '''
    card_values = []
    card_nipes = []
    card_deck = []

    def __init__(self):
        '''
        Constructor
        @todo: Read values for card_values and card_nipes from config file
               Implement the try/finally declaration or delete if not used
               Implement the methods on unittest here
        '''
        self.card_values = ['2', '3', '4', '5', '6', '7', '8', '9',
                            'T', 'J', 'Q', 'K', 'A']
        self.card_nipes = ['S', 'H', 'D', 'C']
        self.card_deck = []

    def mount_deck(self):
        """
        @summary: Method to deal the cards for gamblers
        @todo: Implement this method on Factory class
        """
        try:
            for cv in self.card_values:
                for n in self.card_nipes:
                    self.card_deck.append("%s%s" % (cv, n))
                    del(n)
                del(cv)
            return self.card_deck
        except BaseException as excpt:
            raise excpt
        finally:
            NotImplemented

    def deal_cards(self):
        """
        @summary: Method to deal the cards for gamblers
        @todo: Implement this action according to total of gamblers
            minimun one human x computer or computer x computer
        """
        try:
            gambler_hand = random.choices(self.card_deck, k=5)
            return gambler_hand
        except BaseException as excpt:
            raise excpt
        finally:
            NotImplemented
