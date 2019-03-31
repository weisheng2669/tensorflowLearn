import tensorflow as tf

state =tf.Variable(0,name="counter")
init = tf.initialize_all_variables()   #将所有的变量都初始化
one =tf.constant(1)
add_value =tf.add(state,one)
update = tf.assign(state,add_value)
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))  #不执行sess.run是不可能得到state的，因为tf里面所有的定义只有执行了才有意义

