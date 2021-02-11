import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Diamonds", 7)
        self.cards = [self.card1, self.card2]
        self.CardGame = CardGame()

    def test_check_for_ace__True(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.card1))

    def test_check_for_ace__false(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.card2))

    def test_check_highest_card(self):
        self.assertEqual(self.card2, CardGame.highest_card(self, self.card1, self.card2))

    def test_check_highest_card_changed(self):
        self.card1 = Card("Hearts", 10)
        self.card2 = Card("Spades", 5)
        self.assertEqual(self.card1, CardGame.highest_card(self, self.card1, self.card2))

    def test_check_cards_total(self):
        self.assertEqual("You have a total of 8", CardGame.cards_total(self, self.cards))