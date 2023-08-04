<p align="center"><img width="100%" src="SN.jpg" /></p>

----

# Normalization of Language Embeddings for Cross-Lingual Alignment

Official Repository for the implemention of **Spectral Normalization** from our ICLR 2022 [paper](https://openreview.net/forum?id=Nh7CtbyoqV5):

[**Normalization of Language Embeddings for Cross-Lingual Alignment**](https://openreview.net/forum?id=Nh7CtbyoqV5). Prince Osei Aboaggye, Yan Zheng, Junpeng Wang, Michael Yeh, Wei Zhang, Liang Wang, Hao Yang, Jeff M. Phillips.


This paper proposes a new and general approach to preprocessing (word) embeddings (static and contextual embeddings) called **SPECTRAL NORMALIZATION**. We demonstrated that when this normalization method is used to preprocess monolingual embeddings, it allows alignment procedures to find better alignments, resulting in improved performance on the Bilingual Lexicon Induction (BLI) task as well as Cross-lingual document classification and Cross-lingual natural language inference tasks. Moreover, we demonstrate that this improvement is very broadly useful; it holds in contextual embeddings and embeddings of non-language data (on genomic data).

## Dependencies

* python 
* numpy 

## How To Apply Spectral Normalization

Given a monolingual word embedding (static and contextual embeddings) or any non-language data such as genomic data, you can apply Spectral Normalization with the following command:

```py
python IterSpecNorm.py --input_file INPUT_EMBED --output_file OUTPUT_PATH --niter 5 --max_vocab 200000 --beta 2
```

## Mapping

After preprocessing the embeddings with Spectral Normalization, you can then align the normalized embeddings using libraries such as [MUSE](https://github.com/facebookresearch/MUSE), [VecMap](https://github.com/artetxem/vecmap), etc.

## Citation
If you find anything helpful in this work, please cite our [paper](https://openreview.net/forum?id=Nh7CtbyoqV5):

```
@inproceedings{aboagye2021normalization,
  title={Normalization of Language Embeddings for Cross-Lingual Alignment},
  author={Aboagye, Prince Osei and Zheng, Yan and Yeh, Chin-Chia Michael and Wang, Junpeng and Zhang, Wei and Wang, Liang and Yang, Hao and Phillips, Jeff},
  booktitle={International Conference on Learning Representations},
  year={2021}
}}
```

## Contact

For questions, please email prince@cs.utah.edu

