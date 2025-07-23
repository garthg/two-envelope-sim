import random


def fifty_fifty():
    return random.choice([True, False])


class Game(object):
    # players can't know this or they can infer which envelope they have.
    # in theory needs to be variable up to infinity but we will just have the players ignore it.

    def __init__(self, max_k):
        self.left_id = 'L'
        self.right_id = 'R'
        self.envelopes = {
                self.left_id: None,
                self.right_id: None
            }
        cum_p = random.random()
        k=0
        while True:
            cum_p -= (1/3)*(2/3)**k
            if cum_p < 0:
                break
            k += 1
            if k >= max_k:
                break
        smaller_env = 2 ** k
        left_is_bigger = fifty_fifty()
        self.envelopes[self.left_id] = smaller_env * (2 if left_is_bigger else 1)
        self.envelopes[self.right_id] = smaller_env * (1 if left_is_bigger else 2)

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





def play_switch(g, fc):
    e_id, _ = g.get_envelope(fc)
    _, val = g.switch(e_id)
    return val


def play_stay(g, fc):
    _, val = g.get_envelope(fc)
    return val


n = 10000000
max_k = 30

games = [Game(max_k) for x in range(n)]
first_choice = [fifty_fifty() for x in range(n)]
print('made games and choices')
valid_n = list(filter(lambda x: games[x].get_envelope(first_choice[x])[1] == 32, range(n)))
print(f'got {len(valid_n)} games')

stay = sum(play_stay(games[i], first_choice[i]) for i in valid_n)
switch = sum(play_switch(games[i], first_choice[i]) for i in valid_n)

#print(f'Played {valid_n} games')
print(f'Total for switch:  {switch}')
print(f'Total for stay:    {stay}')
