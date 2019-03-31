import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(-0.5,0.5,200)[:,np.newaxis]
noise = np.random.normal(0,0.02,x_data.shape)
y_data = np.square(x_data)+noise

x = tf.placeholder(tf.float32,[None,1])
y = tf.placeholder(tf.float32,[None,1])

Weights_L1 = tf.Variable(tf.random.normal[1,10])
biases_L1 = tf.Variable(tf.Variable(tf.zeros[1,10]))
Wx_palus_L1 = tf.matmul(x,Weights_L1) +biases_L1

L1=tf.nn.tanh(Wx_palus_L1)

Weights_L2 = tf.Variable(tf.random.normal[10,1])
biases_L2 = tf.Variable(t88)