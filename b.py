import tensorflow as tf
a = tf.Variable([[1,3],[2,4]],dtype = tf.float32)
sess = tf.Session()
sess.run(tf.initlizer_all_variable())
print(a)
