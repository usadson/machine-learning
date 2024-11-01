#!/bin/bash
## Download dataset
wget https://dumps.wikimedia.org/fywiki/20241001/fywiki-20241001-pages-articles.xml.bz2
mv fywiki-20241001-pages-articles.xml.bz2 Data/

## Extraheer alle teksts
python -m wikiextractor.WikiExtractor.py -o friese_wiki_txt Data/fywiki-20241001-pages-articles.xml.bz2

## Voeg het allemaal smaen
cat friese_wiki_txt/* > Data/friese_wiki_corpus.txt

## Maak er een GloVe model van
CORPUS=Data/friese_wiki_corpus.txt
VOCAB_FILE=vocab.txt
COOCCURRENCE_FILE=cooccurrence.bin
COOCCURRENCE_SHUF_FILE=cooccurrence.shuf.bin
BUILDDIR=GloVe/build
SAVE_FILE=friese_vectors
VERBOSE=2
MEMORY=4.0
VECTOR_SIZE=300
MAX_ITER=15
WINDOW_SIZE=10
BINARY=2
NUM_THREADS=8
X_MAX=10

echo "Building vocabulary..."
$BUILDDIR/vocab_count -min-count 5 -verbose $VERBOSE < $CORPUS > $VOCAB_FILE || exit

echo "Counting co-occurrences..."
$BUILDDIR/cooccur -memory $MEMORY -vocab-file $VOCAB_FILE -window-size $WINDOW_SIZE -verbose $VERBOSE < $CORPUS > $COOCCURRENCE_FILE || exit

echo "Shuffling co-occurrences..."
$BUILDDIR/shuffle -memory $MEMORY -verbose $VERBOSE < $COOCCURRENCE_FILE > $COOCCURRENCE_SHUF_FILE || exit

echo "Training GloVe model..."
$BUILDDIR/glove -save-file $SAVE_FILE -threads $NUM_THREADS -input-file $COOCCURRENCE_SHUF_FILE -x-max $X_MAX -iter $MAX_ITER -vector-size $VECTOR_SIZE -binary $BINARY -vocab-file $VOCAB_FILE -verbose $VERBOSE || exit

echo "Training complete. Embeddings saved to $SAVE_FILE.txt"