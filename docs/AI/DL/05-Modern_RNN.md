# 05 | 现代循环神经网络

## Long Short-Term Memory

LSTM mitigates the vanishing/exploding gradient problem
§ Solution: a Memory Cell, updated at each step in the sequence
• Three gates control the flow of information to and from the
Memory Cell
§ Input Gate: protects the current step from irrelevant inputs
§ Output Gate: prevents current step from passing irrelevant information to
later steps
§ Forget Gate: limits information passed from one cell to the next
• Most modern RNN models use either LSTM units or other more
advanced types of recurrent units (e.g., GRU units)
