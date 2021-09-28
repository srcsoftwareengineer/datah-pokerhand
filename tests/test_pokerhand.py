#!/usr/bin/python3.7
'''
Created on 27 de set de 2021
@summary: Unit test for PokerHand class
@author: Sandro Regis Cardoso | Software Engineer
@contact: src.softwareengineer@gmail.com
'''

import unittest

from bin.pokerhand import PokerHand
import random


class Test(unittest.TestCase):

    def test_card_values_0(self):
        objph = PokerHand()
        card_values = objph.card_values
        self.assertEqual(card_values.__len__(), 13)
        del(card_values)

    def test_card_nipes_1(self):
        objph = PokerHand()
        card_nipes = objph.card_nipes
        self.assertEqual(card_nipes.__len__(), 4)
        del(card_nipes)

    def test_mount_deck_2(self):
        try:
            objph = PokerHand()
            card_values = objph.card_values
            card_nipes = objph.card_nipes
            card_deck = []
            for cv in card_values:
                for n in card_nipes:
                    card_deck.append("%s%s" % (cv, n))
                    del(n)
                del(cv)
            self.assertEqual(card_deck.__len__(), (13 * 4))
            del(card_deck)
            del(card_nipes)
            del(card_values)
        except BaseException as excpt:
            raise excpt
        finally:
            NotImplemented

    def test_deal_cards_3(self):
        try:
            ph = PokerHand()
            card_values = ph.card_values
            card_nipes = ph.card_nipes
            card_deck = []
            for cv in card_values:
                for n in card_nipes:
                    card_deck.append("%s%s" % (cv, n))
                    del(n)
                del(cv)
            gambler_cards = random.choices(card_deck, k=5)
            self.assertEqual(gambler_cards.__len__(), 5)
            del(card_deck)
            del(card_nipes)
            del(card_values)
            del(gambler_cards)
        except BaseException as excpt:
            raise excpt
        finally:
            NotImplemented

    def test_parse_cards_4(self):
        """
        @summary: This method evaluate the suit of each card in the
                gambler hands and also from computer as second gambler
        @todo: Implement match/case available in python 3.10
                instead if/elif/else
        """
        ph = PokerHand()
        ph.mount_deck()
        self.assertIsNotNone(ph)

        gambler_cards = ph.deal_cards()
        print(gambler_cards)
        self.assertEqual(gambler_cards.__len__(), 5)

        nipes = ph.card_nipes
        spades = 0
        hearts = 0
        diamonds = 0
        clubs = 0
        for card_value in gambler_cards:
            if card_value[1] == nipes[0]:
                spades += 1
            elif card_value[1] == nipes[1]:
                hearts += 1
            elif card_value[1] == nipes[2]:
                diamonds += 1
            elif card_value[1] == nipes[3]:
                clubs += 1
            else:
                raise Exception

        if hearts == 5:
            # call method checkforflush pontuation
            NotImplemented
        elif spades == 5:
            # call method checkforstraightflush pontuation
            NotImplemented
        else:
            # call method checkfordenomination
            NotImplemented

    def test_checkfor_flush_5(self):
        """
        Method to check for royal flush or flush pontuation
        """
        try:
            strenght = 7
            royalflush = ['AH', 'KH', 'QH', 'JH', 'TH']
            gambler_cards = ['2H', '4H', '8H', '5H', '6H']
            if gambler_cards == royalflush:
                strenght = 1
            return strenght
        except BaseException as excpt:
            raise excpt
        finally:
            NotImplemented

    def test_checkfor_denomination_6(self):
        try:
            strenght = 0
            gambler_cards = ['2C', '2D', '2H', '6S', '6D']
            denominations_list = []
            denominations_match = {}
            initial_match_value = 2
            straight = False
            straight_flush = False
            tree_kind = False
            four_kind = False
            two_ṕair = False
            full_house = False
            one_pair = False
            high_card = False

            for card_value in gambler_cards:
                dval = card_value[0]
                if dval not in denominations_list:
                    denominations_list.append(dval)
                else:
                    if dval not in denominations_match.values():
                        new_dict = {'card_value': dval,
                                    'qty': initial_match_value}
                        denominations_match.update(new_dict)
                    if dval in denominations_match.values():
                        cv = denominations_match.get('card_value')
                        qty = denominations_match.get('qty')
                        print("cv %s qty : %s" % (cv, qty))
                        denominations_match['qty'] = qty + 1
                del(card_value)
                del(gambler_cards)
            return strenght
        except BaseException as excpt:
            raise excpt
        finally:
            NotImplemented

    def test_checkforstraightflush(self):
        NotImplemented


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testInit']
    unittest.main()
