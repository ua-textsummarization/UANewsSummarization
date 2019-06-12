# Text summarization for Ukrainian language

1. **Extractive Summarization**

   This approach weights the important part of sentences and uses the same to form the summary.

   Input article → split into sentences → lemmatize → remove stop words → build a similarity matrix → generate rank based on matrix → pick top N sentences for summary

2. **Deep Learning**

   This approach uses the traditional sequence-to-sequence model with attention. It is customized (mostly inputs/outputs) for the text summarization task.

   Seq2Seq model:

   - uses an encoder (multilayer RNN with LSTM)
   - the decoder is built using a Bahdanau Attention model
   
   
> Additional information:
>
> 1. The dataset with the news in Ukrainian was parsed from <http://texty.org.ua/>.
>
> 2. The embeddings used were downloaded from [here](<http://lang.org.ua/uk/models/>) -- 300d lowercase news Word2Vec.
