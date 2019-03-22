from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
import random
import numpy as np

class Ai:

    def __init__(self, game):
        self.game = game
        self.gamma = 0.9
        self.game_over = 1
        self.model = Sequential()
        self.model.add(Dense(164, init='lecun_uniform', input_shape=(4,)))
        self.model.add(Activation('relu'))
        self.model.add(Dense(150, init='lecun_uniform'))
        self.model.add(Activation('relu'))
        self.model.add(Dense(2, init='lecun_uniform'))
        self.model.add(Activation('linear'))
        self.rms = RMSprop()
        self.model.compile(loss='mse', optimizer=self.rms)

    def receive_state(self, state, epsilon):
        # Set up qval by adding current state to the model
        qval = self.model.predict(state.reshape(1, 4), batch_size=1)
        # We set an epsilon - an ever decreasing number
        # If a random number is less than the epsilon we do a random action
        # If greater we use the qval to decide the action
        # Epsilon stops decreasing at 0.1 so there is always chance of a random action
        # Te random chance means novel action can still happen
        if (random.random() < epsilon):
            action = np.random.randint(0, 2)
        else:
            action = (np.argmax(qval))
        # Take an action now based on the above
        self.take_action(action)
        # Now we check the reward for our action
        reward = self.game.get_reward()
        # Lets find the maximum qvalue that was in the array
        maxQ = np.max(qval)
        # If no reward (no win or lose this cycle)
        # Set the update to be based on the maximum Q value (a decreased value)
        if reward == 0:
            update = reward + (self.gamma * maxQ)
            self.game_over = 0
        # If not the reward itself is the update
        else:
            update = reward
            self.game_over = 1
        # create an empty numpy array y
        y = np.zeros((1,2))
        # make y a copy of qval (original model output)
        y[:] = qval[:]
        # update the up or down value of the qval with the update value calculated above
        # Makes the qval based on the reward
        y[0][action] = update
        # Update the model based on this
        self.model.fit(state.reshape(1, 4), y, batch_size=1, nb_epoch=1, verbose=1)


    def take_action(self, action):
        if action == 0:
            self.game.right_bat.move_down(10)
        else:
            self.game.right_bat.move_up(10)
