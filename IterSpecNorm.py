#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:16:06 2022

@author: kwesi
"""

import numpy as np
from SpecNorm import specNorm 
from argparse import ArgumentParser

def load_embed(filename, max_vocab=-1): 
    words, embeds = [], []
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            word, vector = line.rstrip().split(' ', 1)
            vector = np.fromstring(vector, sep=' ')
            words.append(word)
            embeds.append(vector)
            if len(embeds) == max_vocab:
                break
    return words, np.array(embeds)

def saveEmbed(path, words, word_embeds):
    with open(path, 'w') as f:
        print(word_embeds.shape[0], word_embeds.shape[1], file=f)
        for word, embed in zip(words, word_embeds):
            vector_str = ' '.join(str(x) for x in embed)
            print(word, vector_str, file = f)
            

def main():
    parser = ArgumentParser()
    parser.add_argument('--input_file')
    parser.add_argument('--output_file')
    parser.add_argument('--niter', default=5, type=int)
    parser.add_argument('--max_vocab', default=200000, type=int)
    parser.add_argument('--beta', default=2, type=int)
    args = parser.parse_args()
    
    words, embeds = load_embed(args.input_file, max_vocab=args.max_vocab)
    embeds /= np.linalg.norm(embeds, axis=1)[:, np.newaxis] + 1e-8

    for i in range(args.niter):
        # Center Monoligual Embedding
        embeds -= embeds.mean(axis=0)[np.newaxis, :]
        # Perform Spectral Normalization
        embeds =  specNorm(embeds, args.beta)
        # Unit Length Normalization
        embeds /= np.linalg.norm(embeds, axis=1)[:, np.newaxis] + 1e-8
    saveEmbed(args.output_file, words, embeds)
            
if __name__ == '__main__':
    main()
