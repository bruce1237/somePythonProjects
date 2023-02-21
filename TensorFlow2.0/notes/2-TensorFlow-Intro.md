# TensorFlow 2.0 Introduction
In this notebook you will be given an interactive introduction to TensorFlow 2.0. We will walk through the following topics within the TensorFlow module:

- TensorFlow Install and Setup
- Representing Tensors
- Tensor Shape and Rank
- Types of Tensors


If you'd like to follow along without installing TensorFlow on your machine you can use **Google Collaboratory**. Collaboratory is a free Jupyter notebook environment that requires no setup and runs entirely in the cloud.


## Installing TensorFlow
To install TensorFlow on your local machine you can use pip.
```console
pip install tensorflow
```

If you have a CUDA enabled GPU you can install the GPU version of TensorFlow. You will also need to install some other software which can be found here: https://www.tensorflow.org/install/gpu 
```console
pip install tensorflow-gpu
```


using tensorflow

`import tensorflow as tf`


## tensorflow dataType
```commandline
string = tf.Variable("this is a string", tf.string)
number = tf.Variable(234, tf.int16)
floating = tf.Variable(3.4567, tf.float64)
```

