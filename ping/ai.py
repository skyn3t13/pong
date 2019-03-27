import random
import numpy as np
from ping.data import Data

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import RMSprop, Adam


class Ai:

    def __init__(self, game):
        self.game = game
        self.gamma = 0.9
        self.game_over = 0
        self.model = Sequential()
        self.model.add(Dense(150, init='lecun_uniform', input_shape=(3,)))
        self.model.add(Activation('relu'))
        self.model.add(Dense(168, init='lecun_uniform'))
        self.model.add(Activation('relu'))
        self.model.add(Dense(2, init='lecun_uniform'))
        self.model.add(Activation('linear'))
        self.rms = RMSprop()
        self.model.compile(loss='mse', optimizer=self.rms, metrics=['accuracy'])
        # self.model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
        self.qval = None
        self.action = None
        self.data = Data()


    def receive_state(self, state, epsilon):
        # Set up qval by adding current state to the model
        self.qval = self.model.predict(state.reshape(1, 3), batch_size=1)
        # We set an epsilon - an ever decreasing number
        # If a random number is less than the epsilon we do a random action
        # If greater we use the qval to decide the action
        # Epsilon stops decreasing at 0.1 so there is always chance of a random action
        # Te random chance means novel action can still happen
        if random.random() < epsilon:
            self.action = np.random.randint(0, 2)
        else:
            self.action = (np.argmax(self.qval))
        # Take an action now based on the above
        self.take_action(self.action)
        print(f"Qval is {self.qval}")
        self.data.record_data(ball_x=self.game.ball.rect.x, ball_y=self.game.ball.rect.y,
                              bat_y=self.game.right_bat.rect.y, action=self.action,
                              epsilon=epsilon, reward=self.game.get_reward())


    def update_state(self, state):
        # Now we check the reward for our action
        reward = self.game.get_reward()
        # Lets find the maximum qvalue that was in the array
        max_q = np.max(self.qval)
        # If no reward (no win or lose this cycle)
        # Set the update to be based on the maximum Q value (a decreased value)
        if reward == 0:
            update = reward + (self.gamma * max_q)
            self.game_over = 0
        # If not the reward itself is the update
        else:
            print(f"=== Setting game_over to 1, reward is {reward}")
            update = reward
            self.game_over = 1
        # create an empty numpy array y
        y_val = np.zeros((1, 2))
        # make y a copy of qval (original model output)
        y_val[:] = self.qval[:]
        # update the up or down value of the qval with the update value calculated above
        # Makes the qval based on the reward
        y_val[0][self.action] = update
        # Update the model based on this
        if self.game_over == 1:
            self.model.fit(state.reshape(1, 3), y_val, batch_size=10, nb_epoch=1, verbose=1)
            self.data.new_round(reward)

        print(f"Yval is {y_val}")
        print(update)
        print('-' * 50)
        print(f"Data array: {self.data.record}")
        print(f"Rolling score: {self.data.reward}")
        print(f"Array of scores for each point: {self.data.rewards}")

    def take_action(self, action):
        if action == 0:
            self.game.right_bat.move_down(10)
        else:
            self.game.right_bat.move_up(10)
