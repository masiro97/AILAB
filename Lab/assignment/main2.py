import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

batch_size = 128
test_size = 256

def init_weights(shape):
    return tf.Variable(tf.random_normal(shape,stddev=0.01))

def model(X, w, w2, w3, w4, w_o):
    l1a = tf.nn.relu(tf.nn.conv2d(X,w,strides=[1,1,1,1], padding="SAME"))

    l1 = tf.nn.max_pool(l1a,ksize=[1,2,2,1],strides=[1,2,2,1], padding="SAME")

    l2a = tf.nn.relu(tf.nn.conv2d(l1,w2,strides=[1,1,1,1], padding="SAME"))

    l2 = tf.nn.max_pool(l2a,ksize=[1,2,2,1],strides=[1,2,2,1],padding="SAME")

    l3a = tf.nn.relu(tf.nn.conv2d(l2,w3,strides=[1,1,1,1], padding="SAME"))

    l3 = tf.nn.max_pool(l3a,ksize=[1,2,2,1],strides=[1,2,2,1],padding="SAME")

    l3 = tf.reshape(l3,[-1,w4.get_shape().as_list()[0]])

    l4 = tf.nn.relu(tf.matmul(l3,w4))

    pyx = tf.matmul(l4,w_o)
    return pyx


mnist = input_data.read_data_sets("cifar-100-python/", one_hot=True)
img = mnist.train.images[0].reshape(28,28)
plt.imshow(img,cmap='gray')

trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels
trX = trX.reshape(-1,28,28,1)
teX = teX.reshape(-1,28,28,1)

X = tf.placeholder("float",[None,28,28,1])
Y = tf.placeholder("float",[None,10])

w = init_weights([3,3,1,32])
w2 = init_weights([3,3,32,64])
w3 = init_weights([3,3,64,128])
w4 = init_weights([2048, 625])
w_o = init_weights([625,10])

py_x = model(X,w,w2,w3,w4,w_o)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=py_x, labels=Y))
train_op = tf.train.AdamOptimizer(0.001).minimize(cost)
predict_op = tf.argmax(py_x,1)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for i in range(100):
        training_batch = zip(range(0,len(trX),batch_size)
                             ,range(batch_size,len(trX),batch_size))
        for start, end in training_batch:
            sess.run(train_op,feed_dict={X:trX[start:end], Y:trY[start:end]})

        test_indices = np.arange(len(teX))
        np.random.shuffle(test_indices)
        test_indices = test_indices[0:test_size]

        print(i,np.mean(np.argmax(teY[test_indices],axis=1) ==
                        sess.run(predict_op, feed_dict={X: teX[test_indices],
                                                        Y: teY[test_indices]})))