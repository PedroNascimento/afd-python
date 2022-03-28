# Sigma => Alfabeto de Símbolos de entrada
# Q => Conjunto finito de estados possíveis do autômato
# delta => Função de transição
# q0 => Estado inicial
# F => Conjunto de estados finais

def afd(Sigma, Q, delta, q0, F, cadeia):
    qA = q0 # qA => Estado ativo

    for symbol in cadeia:
        qA = delta[(qA, symbol)]
    return qA in F