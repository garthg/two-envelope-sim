import random


def fifty_fifty():
    return random.choice([True, False])


class Game(object):

    def __init__(self):
        self.left_id = 'L'
        self.right_id = 'R'
        self.envelopes = {
                self.left_id: None,
                self.right_id: None
            }
        left_is_bigger = fifty_fifty()
        if left_is_bigger:
            self.envelopes[self.left_id] = 20
            self.envelopes[self.right_id] = 10
        else:
            self.envelopes[self.left_id] = 10
            self.envelopes[self.right_id] = 20
        # unnecessary, just making the point since it's hardcoded
        left = self.envelopes[self.left_id]
        right = self.envelopes[self.right_id]
        assert ((left_is_bigger and left == 2*right) or (not left_is_bigger and 2*left == right))

    def get_envelope(self, choose_left):
        env_id = self.left_id if choose_left else self.right_id
        return (env_id, self.envelopes[env_id])

    def switch(self, prev_env_id):
        assert (prev_env_id in (self.left_id, self.right_id))
        env_id = self.left_id if (prev_env_id == self.right_id) else self.left_id
        return (env_id, self.envelopes[env_id])


def play_switch():
    g = Game()
    e_id, _ = g.get_envelope(fifty_fifty())
    _, val = g.switch(e_id)
    return val


def play_stay():
    g = Game()
    _, val = g.get_envelope(fifty_fifty())
    return val


n = 1000000

switch = sum(play_switch() for x in range(n))
stay = sum(play_stay() for x in range(n))

print(f'Played {n} games')
print(f'Total for switch: {switch}')
print(f'Total for stay: {stay}')
