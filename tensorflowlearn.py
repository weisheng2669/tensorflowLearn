import tensorflow as tf
m1 = tf.constant([[3,3]])
m2 = tf.constant([[2],[3]])
product = tf.matmul(m1,m2)
# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()
with tf.Session() as sess:  #这里with结束后会自动关闭所有的资源
    result = sess.run(product)
    print(result)