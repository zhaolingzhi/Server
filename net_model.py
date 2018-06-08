from keras.models import Sequential,Model
from keras.layers import Conv2D,MaxPooling2D,Dense,Flatten,\
                         Dropout,Activation,BatchNormalization

from keras.utils.vis_utils import plot_model

path="/home/zlz/PycharmProjects/ag_detection/"


def net_model(name,lr=0.1,decay=0.0001):
    model = Sequential()
    #11.0
    if name == 'Alexnet-simple-gender':
        model.add(Conv2D(96, (7, 7), strides=4, padding='valid',
                         input_shape=(227, 227, 3)))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=2,padding='same'))

        model.add(Conv2D(256, (5, 5), padding='same'))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=2, padding='same'))

        model.add(Conv2D(384, (3, 3), padding='same'))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=2, padding='same'))

        model.add(Flatten())
        model.add(Dense(512))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))

        model.add(Dense(512))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))

        model.add(Dense(2))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('softmax'))
    #3.0
    elif name == 'Alexnet-simple-age':
        model.add(Conv2D(96, (7, 7), strides=4, padding='valid',
                         input_shape=(227, 227, 3)))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=2,padding='same'))

        model.add(Conv2D(256, (5, 5), padding='same'))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=2, padding='same'))

        model.add(Conv2D(384, (3, 3), padding='same'))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=2, padding='same'))

        model.add(Flatten())
        model.add(Dense(512))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))

        model.add(Dense(512))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))

        model.add(Dense(8))
        model.add(BatchNormalization(momentum=0.9))
        model.add(Activation('softmax'))

    print name + " net has been made"
    return model
