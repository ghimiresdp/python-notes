class Game:
    # you can set the width of the box displayed globally
    BOX_WIDTH = 80

    # Menu items to display when game starts
    __menu = {
        1: {
            'name': 'ROCK',
            'symbol': '👊'
        },
        2: {
            'name': 'PAPER',
            'symbol': '🤚'
        },
        3: {
            'name': 'SCISSOR',
            'symbol': '✌️'
        },
        0: {
            'name': 'Restart Game',
            'symbol': '🔂'
        },
        9: {
            'name': 'Quit Game',
            'symbol': '🔄'
        },
    }

    def __init__(self, username):
        self.username = username
        self._matches = 0
        self._draws = 0
        self.computer = 0
        self.user = 0

    def display_menu(self) -> int:
        for id, item in self.__menu.items():
            print(f"{id}. [{item['symbol']}] {item['name']}")
        return int(input("ROCK-PAPER-SCISSOR >> "))


game = Game('Sudip')

game.display_menu()
