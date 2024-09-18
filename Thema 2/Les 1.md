# Thema 2 - Les 1

## Lagen
- Dense Layer = hidden layer?
- activation functie `f`, sigmoid, (clamper?)

- Eerste laag is de `input` laag
- Je laatste is de `output` laag

## Back propagation
Je begint achteraan je weights aanpassen (van achter naar voren)
Je begint met de grootste weight, omdat die de grootste invloed heeft
Totdat voor alle samples je loss minimaal is

## Regulator
$SSE = \Sigma (y-\^{y}) + \lambda \Sigma|B_{;}|$

$y = \alpha + \beta_{1}x + \beta_{2}x + \beta_{n}x$

**Hyperparameter:** $\lambda$

Hiermee stuur je in hoeverre de lijn gaat overfitten

## `relu`
