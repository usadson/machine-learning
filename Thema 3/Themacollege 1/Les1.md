## Les 1: Recurrent Neural Networking

### Tokenization
Het proces vaneen nummertje toewijzen aan woorden of woorddelen.
- [`Tokenizer`](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer) van Keras in de naamruimte `keras.preprocessing.text`.

### Embedding (inbedden)
Woorden die nauwgelegen met elkaar zijn (zoals pizza en kaas, Natalie en Tristan) met elkaar verbinden, en woorden zoals (auto en regenwoud) wat verder bij elkaar weg

Wat twee woorden dichtbij elkaar maakt, zijn de eigenschappen (`features`). Je kunt $N$ eigenschappen allemaal representeren als een as van een ruimte met $N$ dimensies (elk woord heeft een vector in die ruimte). Meestal ligt het aantal dimensies rond het bereik van 50, 100, 200.

Een [`Embedding`](https://keras.io/api/layers/core_layers/embedding/)-laag krijgt dus een getal binnen, en spuugt dan een vector uit met $N$ dimensies.

Om te vergelijken of twee woorden bij elkaar horen, kunnen we het inwendig product pakken van de vectors en zien hoe groot het uitkomstgetal is.

Op dezelfde manier worden inbed-lagen ook getraind met gradient descent, de daadwerkelijke afstand tussen de vectoren van woorden worden vergeleken met de voorspelde afstand, en wordt zodoende getweakt.

Hier wordt [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/) veel voor gebruikt
