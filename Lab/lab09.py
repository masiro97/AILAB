import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

def CNNmodel(X):
#Layer1
    w1 = tf.Variable(tf.random_normal([3,3,1,32],stddev=0.01))
    l1 = tf.nn.relu(tf.nn.conv2d(X,w1,strides=[1,1,1,1],padding='SAME'))
    l1 = tf.nn.max_pool(l1,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')


    w2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev=0.01))
    l2 = tf.nn.relu(tf.nn.conv2d(l1, w2, strides=[1, 1, 1, 1], padding='SAME'))
    l2 = tf.nn.max_pool(l2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    w3 = tf.Variable(tf.random_normal([64*7*7,128],stddev=0.01))
    FC = tf.reshape(l2,[-1,w3.get_shape().as_list()[0]])
    FC = tf.nn.relu(tf.matmul(FC,w3))

    w_o = tf.Variable(tf.random_normal([128,10],stddev=0.01))
    out = tf.matmul(FC,w_o)

    return out

mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)
img = mnist.train.images[0].reshape(28,28)
plt.imshow(img,cmap='gray')
#plt.show()

trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels
trX = trX.reshape(-1,28,28,1)
teX = teX.reshape(-1,28,28,1)

X = tf.placeholder("float",[None,28,28,1])
Y = tf.placeholder("float",[None,10])

batch_size = 128
test_size = 10

CNNout = CNNmodel(X)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=CNNout,labels=Y))
train_op = tf.train.AdamOptimizer(0.001).minimize(cost)
predict_op = tf.argmax(CNNout,1)

init = tf.global_variables_initializer()

with tf.Session() as sess:

    sess.run(init)
    for i in range(test_size):
        training_batch = zip(range(0,len(trX),batch_size),range(batch_size,len(trX),batch_size))
        for start, end in training_batch:
            sess.run(train_op, feed_dict={X: trX[start:end], Y: trY[start:end]})
        test_indices = np.arange(len(teX))
        np.random.shuffle(test_indices)
        test_indices = test_indices[0:test_size]

        print(i,np.mean(np.argmax(teY[test_indices],axis=1) == sess.run(predict_op,feed_dict={
                X: teX[test_indices], Y: teY[test_indices]})))