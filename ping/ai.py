from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
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

    def receive_state(self, state):
        print(self.model.predict(state.reshape(1, 4), batch_size=1))

