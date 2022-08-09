# Making the word jumble game multiplayer

class game:

    def __init__(self, name, age, level=1):
        pass

    def run(self):
        pass

    def results(self):
        return (self.name, self.score)

# -------------------------------------------------

if __name__ == '__main__':
    
    players = [('Anusha', 20), ('Naveen', 20), ('Vishal', 20)]

    pobjs = []
    for name, age in players:
        pobjs.append(game(name, age))

    for obj in pobjs:
        obj.run()

    print('FINAL SCORES ')
    for obj in pobjs:
        t = obj.results()
        print(t[0], ' ----> ', t[1])

