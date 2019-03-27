from tensorflow.examples.tutorials.mnist import input_data
import os
import scipy.misc
import numpy as np
mnist = input_data.read_data_sets("D:\\tensorflowData",one_hot=True) #训练数据集,和测试数据集
# print(mnist.train.images.shape) #打印有多少个训练图片
# print(mnist.train.labels.shape)
# print(mnist.train.images[0,:])
print(mnist.train.labels[0,:])  #打印第0个标签的内容
# save_dir = 'D:\\tensorflowData\\raw'  #创建下载图片地址的工作
# if os.path.exists(save_dir) is False:
#     os.makedirs(save_dir)
# for i in range(20):   #下载前20张图片到本地
#     image_array = mnist.train.images[i,:]
#     image_array = image_array.reshape(28,28)
#     filename =save_dir+'mnist_train_%d.jpg'%i
#     scipy.misc.toimage(image_array,cmin=0.0,cmax=1.0).save(filename)

for i in range(20):
    one_hot_label =mnist.train.labels[i,:]
    label = np.argmax(one_hot_label)
    print('mnist_train_%d.jpg label  %d' % (i,label))
