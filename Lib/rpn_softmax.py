# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 02:54:21 2017

@author: Kevin Liang
"""

import tensorflow as tf

def rpn_softmax(rpn_cls_score):
    '''
    Reshape the rpn_cls_score (1,W,H,2k) to take a softmax. Converts scores to 
    probabilities
    
    ex. 9 anchors, 1 image minibatch, convolutional feature maps of dims WxH
    
    rpn_cls_score: (1,W,H,18)
    <transpose>     (1,18,W,H)
    <reshape>       (1,2,9W,H)
    <transpose>     (1,9W,H,2)
    <softmax>       (1,9W,H,2)
    <transpose>     (1,2,9W,H)
    <reshape>       (1,18,W,H)
    <transpose>     (1,W,H,18)
    
    return rpn_cls_prob
    '''    
    
    # input shape dimensions
    shape = tf.shape(rpn_cls_score)
    
    # Reshape rpn_cls_score to prepare for softmax
    rpn_cls_score = tf.transpose(rpn_cls_score,[0,3,1,2])
    rpn_cls_score = tf.reshape(rpn_cls_score,[shape[0],2,shape[3]/2*shape[1],shape[2]])
    rpn_cls_score = tf.transpose(rpn_cls_score,[0,2,3,1])
    
    # Softmax
    rpn_cls_prob = tf.nn.softmax(rpn_cls_score)
    
    # Reshape back to the original
    rpn_cls_prob = tf.transpose(rpn_cls_prob,[0,3,1,2])
    rpn_cls_prob = tf.reshape(rpn_cls_prob,[shape[0],shape[3],shape[1],shape[2]])
    rpn_cls_prob = tf.transpose(rpn_cls_prob,[0,2,3,1])
    
    return rpn_cls_prob