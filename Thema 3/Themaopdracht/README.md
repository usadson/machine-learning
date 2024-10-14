# OERbotje
- Zelf onderzoek
- Chatbot voor onderwijs- en examenreglement (ook HBO-I?)
- Niet zelf helemaal trainen, een bestaand LLM uit te breiden met deze kennis

dmv RAG: Retrieval Augmented Generation
- voeren aan een semantische databank (SemDB)
- haalt de meest vergelijkbare record op, obv embedding space
- aan een LLM vraag je dan, samen met de relevante data uit de SemDB en de originele vraag, om het antwoord te formuleren
- [voorbeeld](https://medium.com/@xvtjy/rag-implementation-using-keras-nlp-and-chromadb-34c6868dd908) duurt 2 uur

## stappenplan
- bekijk voorbeelden en uitleg op brightspace
- kies een Semantisch databank (bijv )
- train dan deze met de reglement en HBO-I
- Nederlandssprekend LLM bijvoorbeeld Geitje
- gebruik GUFF ipv keras_nlp, met bijv OLlama


## oplevering
- geen notebooks
- maar een werkende gui
- met flask bijv.
