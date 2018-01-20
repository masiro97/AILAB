import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# x = tf.constant(([10,20],[30,40]))
# with tf.Session() as sess:
#     print (x)
#     print (sess.run(x))

# x = tf.Variable(10)
# init = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init)
#     print (x)
#     print (sess.run(x))

# Example_multiply

# a = tf.placeholder("float32")
# b = tf.placeholder("float32")
#
# y = tf.multiply(a,b)
#
# with tf.Session() as sess:
#     print (sess.run(y,feed_dict={a:2.0,b:5.0}))

#Example_Operation

# matrix1 = np.array([(1,1,1),(1,1,1),(1,1,1)],dtype='float32')
# matrix2 = np.array([(2,2,2),(2,2,2),(2,2,2)],dtype='float32')
#
# tf_matrix1 = tf.constant(matrix1)
# tf_matrix2 = tf.constant(matrix2)
#
# matrix_mul = tf.matmul(tf_matrix1,tf_matrix2)
#
# with tf.Session() as sess:
#     print (tf_matrix1)
#     print (matrix_mul)
#     print (sess.run(matrix_mul))

#Linear Regression



linalg = np.linalg
np.random.seed(1)

num_samples = 1000
num_variables = 2
cov = [[0.3,0.2],[0.2,0.2]]

L = linalg.cholesky(cov)

uncorrelated = np.random.standard_normal((num_variables,num_samples))
mean = [1,1]
correlated = np.dot(L,uncorrelated) + np.array(mean).reshape(2,1)

x_data = correlated[0,:]+1
y_data = correlated[1,:]+1
plt.scatter(x_data,y_data,c='green')
plt.show()

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
B = tf.Variable(tf.zeros([1]))

h = W * x_data + B

cost_function = tf.reduce_mean(tf.square(h-y_data))

alpha = tf.Variable(0.015)
optimizer = tf.train.GradientDescentOptimizer(alpha)
train = optimizer.minimize(cost_function)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for step in range(201):
        sess.run(train)
        if(step == 0 or step == 5 or step == 10 or step == 200):
            plt.plot(x_data,y_data,'o',label='step={}'.format(step))
            plt.plot(x_data,(sess.run(W) * x_data + sess.run(B)),'-')
            plt.legend()
            plt.xlim(0,5)
            plt.ylim(0,4)
            plt.show()
    print(sess.run(W),sess.run(B))