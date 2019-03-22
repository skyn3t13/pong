from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
import random
import numpy as np

class Ai:

    def __init__(self):
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
        qval = self.model.predict(state.reshape(1, 4), batch_size=1)
        if (random.random() < epsilon):
            action = np.random.randint(0, 2)
        else:
            action = (np.argmax(qval))
            print("2nd" + str(action))
