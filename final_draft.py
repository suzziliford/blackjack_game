import requests
import time
deck_id = '8kbdejolek8w'

base_url = 'https://www.deckofcardsapi.com/' 

class Deck():

    def draw_request(self):
        deck_draw = requests.get("https://www.deckofcardsapi.com/api/deck/new/draw/?count=1")
        card = deck_draw.json()
        value = card['cards'][0]['value']
        suit = card['cards'][0]['suit']
        # print(card['cards'][0]['value'])
        trimmed_card = {'value':value, 'suit':suit}      
        # return f"{self.rank} of {self.suit}"
        # print(trimmed_card.values())
        return trimmed_card

    def __str__(self):
        return f"{self.value} of {self.suit}"
    

    def assess_cards(self):
        card_nums = []
        aces = []
        royalty = []
        total = []
        for card in Player.player_score:
            if len(card) <= 2:
                card_nums.append(card)
            elif card == 'ACE':
                aces.append(card)
            else:
                royalty.append(card)

        total = list(map(int, card_nums))
        
        
        for card in range(len(aces)):
            card = int(11)
            total.append(card)
    

        for card in range(len(royalty)):
            card = int(10)
            total.append(card)
        
        
        total = sum(total)
        return total

    @property
    def value(self):
        if self.value == 'ace':
            count = 11
        else:
            try:
                count = int(self.value)
            except:
                 count = 10
        return count


class Player():
    hand = []
    player_score = []
    def __init__(self, name):
        self.name = name

    def add_card(self, card):
        self.hand.append(card)
    
    def assess_cards(self):
        card_nums = []
        aces = []
        royalty = []
        self.total = []
        for card in Player.player_score:
            if len(card) <= 2:
                card_nums.append(card)
            elif card == 'ACE':
                aces.append(card)
            else:
                royalty.append(card)

        self.total = list(map(int, card_nums))
        
        
        for card in range(len(aces)):
            if len(aces)>1:
                aces[0] = 11
                aces[1] = 1
            else:
                aces[0] = 11
            
        for card in aces:
            self.total.append(card)
    

        for card in range(len(royalty)):
            card = int(10)
            self.total.append(card)
        
        
        self.total = sum(self.total)
        return self.total
        
    def ace_variation(self):
        new_total = 0
        if Player.assess_cards(self) > 21:
            if 'ACE' in Player.player_score:
                new_total == (Player.assess_cards(self)-10)
        return new_total


class Dealer():
    dealer_hand = []
    dealer_score = []

    def dealer_add_card(self,card):
        self.dealer_hand.append(card)

    def show_hand(self):
        #show hand
        pass

    def assess_cards():
        card_nums = []
        aces = []
        royalty = []
        total = []
        for card in Dealer.dealer_score:
            if len(card) <= 2:
                card_nums.append(card)
            elif card == 'ACE':
                aces.append(card)
            else:
                royalty.append(card)

        total = list(map(int, card_nums))
        
        
        for card in range(len(aces)):
            if len(aces)>1:
                aces[0] = 11
                aces[1] = 1
            else:
                aces[0] = 11
            
        for card in aces:
            total.append(card)
    

        for card in range(len(royalty)):
            card = int(10)
            total.append(card)
        
        
        total = sum(total)
        return total

    def ace_variation():
        new_dealer_total = 0
        if Dealer.assess_cards() > 21:
            if 'ACE' in Dealer.dealer_score:
                new_dealer_total = (Dealer.assess_cards()-10)
        return new_dealer_total



class GameBoard():
    game_deck = Deck()
    #tell them your name
    print(
        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        >>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Welcome to Blackjack//////////////////
        >>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        >>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        """
    )

    time.sleep(1)
    name = input("What is your name?: ")
    this_player = Player(name) 
    dealer = Dealer()
    #input queues
    
    player_card1 = game_deck.draw_request()
    card1_values = list(player_card1.values())
    Player.player_score.append(card1_values[0])
    # print(Player.player_score)
    
    # player_card1 = str(player_card1)
    this_player.add_card(player_card1)
    print(f"You first card is a {card1_values[0]} of {card1_values[1]}")
    print('='*29)
    time.sleep(2)

    
    dealer_card1 = game_deck.draw_request()
    dealer_card1_values = list(dealer_card1.values())
    Dealer.dealer_score.append(dealer_card1_values[0])
    dealer.dealer_add_card(dealer_card1)
    # dealer_card2 = str(dealer_card1)
    print (f"Dealer was dealt a {dealer_card1_values[0]} of {dealer_card1_values[1]}")
    
    time.sleep(1)

    # Dealer.hand.append(game_deck.draw_request())
    # print(Dealer.hand)
    dealer_card2 = game_deck.draw_request()
    dealer_card2_values = list(dealer_card2.values())
    Dealer.dealer_score.append(dealer_card2_values[0])
    
    print (f"Plus a 2nd card which is hidden")
    print('='*29)
    time.sleep(2)

    player_card2 = game_deck.draw_request()
    card2_values = list(player_card2.values())
    Player.player_score.append(card2_values[0])
    this_player.add_card(player_card2)
    print (f"Your second card is {card2_values[0]} of {card2_values[1]}")
    time.sleep(2)
    print ("Which brings your total to: " )
    time.sleep(1)
    print(this_player.assess_cards())
    time.sleep(2)
    print('='*29)


    if this_player.assess_cards() == 21:
        #you win
        print('Blackjack! You Win')
        # print('='*29)
        

    else: 
        hitting = True
        while hitting:
            hit = input('do you want to hit or stay(type hit/stay): ').lower()

            if hit == 'hit':
                hit_card = game_deck.draw_request()
                hit_card_values = list(hit_card.values())
                Player.player_score.append(hit_card_values[0])
                this_player.add_card(hit_card)
                time.sleep(1)
                print (f"You were dealt the card {hit_card_values[0]} of {hit_card_values[1]}")
                time.sleep(2)
                # if this_player.assess_cards() > 21:
                #     if "ACE" in this_player.player_score:
                #         Player.ace_variation(this_player)
                #         this_player.assess_cards = this_player.ace_variation
                # print('='*29)
                print ("Which brings your total to: " )
                print(this_player.assess_cards())
                time.sleep(1)
                if this_player.assess_cards() == 21:
                    print('Blackjack! You win')
                    print('='*29)
                    break
                # elif this_player.assess_cards() < 21:
                #     if 'ACE' in Player.player_score():
                #         this_player.assess_cards = (this_player.assess_cards-int(10))
                elif this_player.assess_cards() <= 21:
                    hitting = True
                elif this_player.assess_cards() >= 21:
                    print('BUST!')
                    hitting = False
                    time.sleep(2)
                    break
            elif hit == 'stay':
                hitting = False
            else:
                print("Please type hit or stay")

    print('='*29)
    print(f"Dealer reveals their second card, {dealer_card2_values[0]} of {dealer_card2_values[1]}")
    time.sleep(2)
    print("Which brings their total to")
    print((Dealer.assess_cards()))
    time.sleep(2)
    print('='*29)

    while Dealer.assess_cards() <= 17:
        dealer_card3 = game_deck.draw_request()
        dealer_card3_values = list(dealer_card3.values())
        Dealer.dealer_score.append(dealer_card3_values[0])
        print(f"Dealer was dealt {dealer_card3_values[0]} of {dealer_card3_values[1]}")
        Dealer.ace_variation()
        time.sleep(2)
        print("Which brings dealer's total to")
        print(Dealer.assess_cards())
        time.sleep(2)

    if Dealer.assess_cards() > 21 and this_player.assess_cards()< 21:
        print("Dealer is BUST. You Win")
    elif Dealer.assess_cards() < 21 and Dealer.assess_cards() > this_player.assess_cards():
        print("Dealer wins")
    elif Dealer.assess_cards() > 21 and this_player.assess_cards() > 21:
        print("Double Bust. Nobody Wins")
    elif this_player.assess_cards() < 21 and this_player.assess_cards() > Dealer.assess_cards():
    # Dealer.assess_cards() < 21 and Dealer.assess_cards() < this_player.assess_cards():
        print("You Win")
    elif Dealer.assess_cards()>21 and this_player.assess_cards()==21:
        print("Dealer is BUST. You Win")
    elif Dealer.assess_cards()<21 and this_player.assess_cards()==21:
        print("You Win") 
    elif Dealer.assess_cards()<21 and Dealer.assess_cards() == this_player.assess_cards():
        print("Draw. Nobody Wins")
    elif Dealer.assess_cards() < 21 and this_player.assess_cards() > 21:
        print("Dealer Wins")
    elif Dealer.assess_cards() > 21:
        print("Dealer is BUST")
    elif Dealer.assess_cards() == 21:
        print("Blackjack! Dealer Wins")
    elif Dealer.assess_cards() == 21 and this_player.assess_cards() == 21:
        print("Draw. Nobody Wins")

deck = Deck()


game = GameBoard()