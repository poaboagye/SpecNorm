# Normalization of Language Embeddings for Cross-Lingual Alignment

Repository for the implemention of **Spectral Normalization** from our ICLR 2022 [paper](https://openreview.net/forum?id=Nh7CtbyoqV5):

[**Normalization of Language Embeddings for Cross-Lingual Alignment**](https://openreview.net/forum?id=Nh7CtbyoqV5). Prince Osei Aboaggye, Yan Zheng, Junpeng Wang, Michael Yeh, Wei Zhang, Liang Wang, Hao Yang, Jeff Phillips.


This paper proposes a new and general approach to preprocessing (word) embeddings (static and contextual embeddings) called SPECTRAL NORMALIZATION. We demonstrated that when this normalization method is used to preprocess monolingual embeddings, it allows alignment procedures to find better alignments, resulting in improved performance on the Bilingual Lexicon Induction (BLI) task as well as Cross-lingual document classification and Cross-lingual natural language inference tasks. Moreover, we demonstrate that this improvement is very broadly useful; it holds in contextual embeddings and embeddings of non-language data (on genomic data).

## How To Apply Spectral Normalization

Given a monoligual word embedding (static and contextual embeddings) or any non-language data such as genomic data, you can apply Spectral Normalization with the following command:


