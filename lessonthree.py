import tensorflow as tf

x = tf.Variable([1,2])
y = tf.constant([3,3])
sub = tf.subtract(x,y)
add = tf.add(x,sub)
update = tf.assign(x,add)   #赋值操作 ,若对y进行赋值的话会出错，因为它不是常量
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))
    print(sess.run(update))