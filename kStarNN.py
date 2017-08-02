#!/usr/bin/env python3
#coding="utf-8"

"""
K*-nearest-neighbor graph 

Reference:
2016 NIPS,Oren Anava,Kfir Levy,"k*-nearest Neighbors: From Global to Local"
"""

import sys
import numpy as np
import scipy as sp

class kStarNN:

    def __init__(self):
        pass

    def generateGraph(self, data_file, libschitz_noise_ratio):
        """ load data from data file and generate kStarNN graph.
        the generated graph is stored in adjacent list format

        parameters:
            data_file -- input data matrix, each row is a sample.
            libschitz_noise_ratio -- hyperparameter, control the bound of "k*"
        """
       
        # step 1, for each sample, we calculate the distance between itself and
        # samples. and then sort.




    def one_to_others_distances(self,
                                idx,
                                data=np.array(),
                                metric="euclidean"):
        """ calculate the distance between sample "idx" and other rows in
        matrix data. When calculate the distance, we set the distance
        between "idx" and itself to the
        MAXIMUM INT value.

        parameters:
            idx -- row index of current sample
            data -- numpy array data matrix, each row is a sample
        return:
            dist -- one row of nparray of distances.
        """

        (n,m) = data.shape # n: number of samples, m: number of features

        if (idx < 0 || idx >= n)
            print("Error, idx value out of range!")
            return

        s = data[idx,:]

        dist = sp.spatial.distance.cdist(s,data,metric);

        return dist



    


