# Text summarization for Ukrainian language

1.  **Extractive Summarization**

This approach weights the important part of sentences and uses the same to form the summary.

Input article → split into sentences → lemmatize → remove stop words → build a similarity matrix → generate rank based on matrix → pick top N sentences for summary


2. **Deep Learning**

Seq2Seq model:
- Encoder-Decoder
- Bidirectional RNN
- Bahdanau Attention
- Adam Optimizer
- exponential or cyclic learning rate
- Beam Search or Greedy Decoding
