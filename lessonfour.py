import tensorflow as tf
#Fecth 可以再一个run中定义多个操作一次性输出
m1 = tf.constant(1.0)
m2 = tf.constant(2.0)
m3 = tf.constant(3.0)

add = tf.add(m1,m2)
mut = tf.multiply(m3,add)
#
# with tf.Session() as sess:
#     result = sess.run([mut,add])
#     print(result)

#Feed  ##feed 的数据以字典的形式传入
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1,input2)
with tf.Session() as sess:
     print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))