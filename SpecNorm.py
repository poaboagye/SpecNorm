#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:15:11 2022

@author: kwesi
"""

import numpy as np

def computeSVD(embed):
    """
    Args:
        emded: Monolingual Embedding    

    Returns:
        Singular Value Decompostion
    """
    U, S, VT = np.linalg.svd(embed,full_matrices=False)
    return U, S, VT

def specNorm(embed, beta):
    """
    Args:
        emded: Monolingual Embedding
        beta: Use to determine smaller (noisy) 
        singular values to be removed

    Returns:
        Spectral Normalised Embedding
    """
    # Perform SVD on the Data
    _, S, VT = computeSVD(embed)
    # Compute eta
    eta = np.sqrt(np.sum(S**2)/len(S))
    # Transform  diagonal matrix
    S_prime = 1 / S
    for idx, sigma in enumerate(S):
        if sigma > beta*eta:
            S_prime[idx] = S_prime[idx] * (beta*eta)
        else:
            S_prime[idx] = 1
    S_prime = np.eye(len(S)) * S_prime   
    # Compute new monolingual embedding     
    embed = embed @ VT.T @ S_prime
    return embed









    
    

























