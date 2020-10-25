import  random
class LotoCard:
    def __init__(self, player):
        self.player = player
        self.my_card()

    def my_card(self):
        self.card = []
        i = 1
        while i <= 3:
            my_list = []
            a = 0
            b = 0
            while a < 5:
                my_list.insert(a, random.randint(1, 91))
                a += 1
            while b < 4:
                my_list.insert(random.randint(0, 9), ' ')
                b += 1
            self.card.insert(i, my_list)
            i += 1



    def __str__(self):
      return f"{self.player}" + "\n" +"-" * 30 + "\n" + '\n'.join([' '.join([str(elem) for elem in line]) for line in self.card]) + "\n" + "-" * 30



class LotoGame:
    pass


human_player = LotoCard('Игрок')
computer_player = LotoCard("Компьютер")
# game = LotoGame(human_player, computer_player)
print(human_player)
print(computer_player)
