import tensorflow as tf
import numpy as np

idx2char = ['h','e','l','o']
x_data = [[0,1,2,2]]
x_one_hot = [[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,1,0]]]
y_data = [[1,2,2,3]]

#parameter
num_classes = 4
input_dim = 4 #one-hot size
hidden_size = 4 #output from the LSTM
batch_size = 1 # one sentence
sequence_length = 4 #ello = 4
learning_rate = 0.1

X = tf.placeholder(tf.float32,[None,sequence_length,input_dim]) # X one-hot
Y = tf.placeholder(tf.int32,[None,sequence_length]) # Y label

cell = tf.contrib.rnn.BasicLSTMCell(num_units = hidden_size)
initial_state = cell.zero_state(batch_size,tf.float32)
outputs, _states = tf.nn.dynamic_rnn(cell,X,initial_state=initial_state,dtype=tf.float32)

weights = tf.ones([batch_size,sequence_length])
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs, targets=Y,weights=weights)
loss = tf.reduce_mean(sequence_loss)
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)
prediction = tf.argmax(outputs,axis=2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(50):
        L,_ = sess.run([loss,train],feed_dict={X: x_one_hot, Y: y_data})
        result = sess.run(prediction,feed_dict={X: x_one_hot})
        print(i,"loss:",L,"prediction:",result,"true Y:",y_data)

        #print char using dic
        result_str = [idx2char[c] for c in np.squeeze(result)]
        print("\tPrediction str: ",''.join(result_str))