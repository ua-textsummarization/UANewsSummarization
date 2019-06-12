# Text summarization for Ukrainian language

> Relevant information:
>
> 1. There was no suitable dataset for news in Ukrainian so we parsed the articles ourselves from <http://texty.org.ua/>.
> 2. In the first approach in the file **text_processing.py** we perform our own lemmatization and tokenization of the dataset.
> 3. The embeddings that we used in the second approach were downloaded from the [lang-uk](<http://lang.org.ua/uk/models/>) website—the particular one is the **300d lowercase news Word2Vec**.

1. **Extractive Summarization**

   Extractive methods attempt to summarize articles by selecting a subset of words that retain the most important points, i.e. this approach weights the important part of sentences and uses the same to form the summary. We define weights for the sentences and further rank them based on importance and similarity among each other. Basically the algorithm goes as follows:

   Input article → split into sentences → lemmatize → remove stop words → build a similarity matrix → generate rank based on matrix → pick top N sentences for summary

2. **Deep Learning for Abstractive Summarization**

   Abstractive summarization, ideally, is closer to how a human would summarize a large document. In practice, it's very hard to implement. The goal of abstractive summarization is to _generate_ sentences describing the content of the document, often using words and phrases that weren't even used in the original. In our case we used a traditional sequence-to-sequence model with attention. This model is specifically customized for the text summarization task.

   Seq2Seq model:

   - uses an encoder (multilayer RNN with LSTM)
   - the decoder is built using a Bahdanau Attention model

Example of extractive summarization from our code:

![alt text](<https://github.com/ua-textsummarization/UANewsSummarization/blob/master/images/summarization1.PNG>)

![alt text](<https://github.com/ua-textsummarization/UANewsSummarization/blob/master/images/summarization2.PNG>)

