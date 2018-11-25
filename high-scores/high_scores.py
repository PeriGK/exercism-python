class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def highest(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def top(self):
        return sorted(self.scores, reverse=True)[0:3]

    def report(self):
        latest_score = self.latest()
        best_score = self.highest()
        if latest_score == best_score:
            msg = "Your latest score was {}. That's your personal best!".format(best_score)
        else:
            msg = "Your latest score was {}. That's {} short of your personal best!".format(latest_score, best_score - latest_score)

        return (msg)