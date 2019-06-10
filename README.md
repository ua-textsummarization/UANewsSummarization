# Text summarization for Ukrainian language

1. Bruteforce

Input article → split into sentences → remove stop words → build a similarity matrix → generate rank based on matrix → pick top N sentences for summary


2. Deep Learning

**Seq2Seq model**
- Encoder-Decoder
- Bidirectional RNN
- Bahdanau Attention
- Adam Optimizer
- exponential or cyclic learning rate
- Beam Search or Greedy Decoding
