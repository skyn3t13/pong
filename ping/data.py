class Data:

    def __init__(self):
        self.record = []
        self.make_hash()
        self.rewards = []
        self.reward = 0

    def record_data(self, ball_x, ball_y, bat_y, action, epsilon, reward):
        self.record[-1]["ball_x"] = ball_x
        self.record[-1]["ball_y"] = ball_y
        self.record[-1]["bat_y"] = bat_y
        self.record[-1]["action"] = action
        self.record[-1]["epsilon"] = epsilon
        self.reward += reward

    def new_round(self, reward):
        self.make_hash()
        self.reward += reward
        self.rewards.append(self.reward)
        self.reward = 0
        print("New round is triggered!!")

    def make_hash(self):
        self.record.append({"ball_x": None, "ball_y": None, "bat_y": None, "action": None, "epsilon": None})



