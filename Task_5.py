class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
    
    def number_of_wins(self):
        return f'Футбольных побед: {self.victories}'
    def number_of_draws(self):
        return f'Футбольных ничьих: {self.draws}'
    def number_of_losses(self):
        return f'Футбольных поражений:  {self.losses}'
    def total_points(self):
        return f'Общее количество очков: {3*self.victories + self.draws}'
    
class Hockey(Results): 
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        return f'Хоккейных побед: {self.victories}'
    def number_of_draws(self):
        return f'Хоккейных ничьих: {self.draws}'
    def number_of_losses(self):
        return f'Хоккейных поражений:  {self.losses}'
    def total_points(self):
        return f'Общее количество очков: {2*self.victories + self.draws}'
    

football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

football_methods = ['number_of_wins', 'number_of_draws', 'number_of_losses', 'total_points']
for method in football_methods:
    print(getattr(football_team, method)())

hockey_methods = ['number_of_wins', 'number_of_draws', 'number_of_losses', 'total_points']
for method in hockey_methods:
    print(getattr(hockey_team, method)())