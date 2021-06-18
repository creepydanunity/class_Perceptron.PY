import random as rnd


class poker_table:
    def __init__(self, max_players=6):
        self.max_players = max_players
        self.prev_bet = 2
        self.players = []
        self.__new_pack()
        self.state = 'Before'

    def __new_pack(self):
        self.cards = [i for i in range(1, 53)]
        parts = [' of Hearts', ' of Spades', ' of Clubs', ' of Diamonds']
        names = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
        self.card_names = []
        for name in names:
            for part in parts:
                self.card_names.append(name.capitalize() + part)

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        self.__new_pack()

        for player in self.players:
            if player.value <= 0:
                self.players.remove(player)

        if len(self.players) > 2:
            for player in self.players:
                self.cards = player.new_cards(self.cards)
            self.state = 'Playing'
        else:
            print(f'Too low amount of Players: {len(self.players)} / 3.')

    def __str__(self):
        if self.state == 'Before':
            player_info = ''
            idx = 1
            for player in self.players:
                player_info += '\n' + f'Seat #{idx} ' + str(player)
                idx += 1
            return f'Current Players: ' + player_info
        else:
            player_info = ''
            idx = 1
            for player in self.players:
                player_info += '\n' + f'Seat #{idx} ' + str(player) + ' Cards: ' \
                               + self.card_names[player.cards[0] - 1] + ', ' \
                               + self.card_names[player.cards[1] - 1] + '.'
                idx += 1
            return f'Current Players: ' + player_info

class poker_player:
    def __init__(self, nickname, table: poker_table, value=100):
        self.value = value
        self.table = table
        self.name = nickname
        self.cards = []
        self.state = 'Start'

    def __str__(self):
        return f'Player: {self.name}, money: {self.value}.'

    def __get_cards(self):
        if self.cards:
            return f'{self.name}: {" ".join(self.cards)}.'

    def new_cards(self, pack):
        rnd.shuffle(pack)
        self.__check()
        self.cards = [0, 0]
        while self.cards[0] == self.cards[1]:
            self.cards = rnd.choices(pack, k=2)
        self.state = 'Play'
        for card in self.cards:
            pack.remove(card)
        return pack

    def bet(self, big_blind=2):
        b = self.value + 1
        while big_blind > b > self.value:
            b = input(input(str(self) + ' Bet: '))
        self.value -= b
        self.__check()
        return b

    def ps(self):
        self.cards = []
        self.state = 'Pass'

    def call(self, value=2):
        if self.value >= value:
            self.value -= value
            return value
        elif self.state == 'Play':
            self.value -= self.value
            self.__check()
            return self.value
        else:
            return str(self)

    def __check(self):
        if self.value == 0:
            self.state = 'All'

    def raising(self):
        pass


table_1 = poker_table(4)
player_1 = poker_player('P_1', table_1)
player_2 = poker_player('P_2', table_1)
player_3 = poker_player('P_3', table_1, value=0)
table_1.add_player(player_1)
table_1.add_player(player_2)
table_1.add_player(player_3)
table_1.start_game()
print(table_1)