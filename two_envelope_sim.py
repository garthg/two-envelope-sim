import random


def fifty_fifty():
    return random.choice([True, False])


class Game(object):
    # players can't know this or they can infer which envelope they have.
    # in theory needs to be variable up to infinity but we will just have the players ignore it.
    _secret_max = 1234.5

    def __init__(self):
        self.left_id = 'L'
        self.right_id = 'R'
        self.envelopes = {
                self.left_id: None,
                self.right_id: None
            }
        left_is_bigger = fifty_fifty()
        bigger = random.random()*self._secret_max
        if left_is_bigger:
            self.envelopes[self.left_id] = bigger
            self.envelopes[self.right_id] = bigger/2.0
        else:
            self.envelopes[self.left_id] = bigger/2.0
            self.envelopes[self.right_id] = bigger
        # unnecessary, just making the point since it's hardcoded
        left = self.envelopes[self.left_id]
        right = self.envelopes[self.right_id]
        assert ((left_is_bigger and left == 2*right) or (not left_is_bigger and 2*left == right))

    def get_envelope(self, choose_left):
        env_id = self.left_id if choose_left else self.right_id
        return (env_id, self.envelopes[env_id])

    def switch(self, prev_env_id):
        assert (prev_env_id in (self.left_id, self.right_id))
        env_id = self.left_id if (prev_env_id == self.right_id) else self.right_id
        return (env_id, self.envelopes[env_id])



# this game is NOT the two envelopes problem, but it's what it feels like maybe it is
class GamePostHoc(object):
    _secret_max = 1234.5

    def __init__(self):
        self.left_id = 'L'
        self.right_id = 'R'
        self.first_value = random.random()*self._secret_max

    def get_envelope(self, choose_left):
        env_id = self.left_id if choose_left else self.right_id
        return (env_id, self.first_value)

    def switch(self, prev_env_id):
        env_id = self.left_id if (prev_env_id == self.right_id) else self.right_id
        new_val_bigger = fifty_fifty()
        new_val = None
        if new_val_bigger:
            new_val = 2.0*self.first_value
        else:
            new_val = 0.5*self.first_value
        return (env_id, new_val)



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
print(f'Total for switch:  {switch}')
print(f'Total for stay:    {stay}')
