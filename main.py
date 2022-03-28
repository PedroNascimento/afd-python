from function_afd import afd

Sigma = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']
Q = ['q0', 'q1', 'q2']
F = ['q2']
delta = {
    ('q0', '0'): 'q0',
    ('q0', '1'): 'q0',
    ('q0', '2'): 'q0',
    ('q0', '3'): 'q0',
    ('q0', '4'): 'q0',
    ('q0', '5'): 'q0',
    ('q0', '6'): 'q0',
    ('q0', '7'): 'q0',
    ('q0', '8'): 'q0',
    ('q0', '9'): 'q0',
    ('q0', ','): 'q1',
    ('q1', '0'): 'q2',
    ('q1', '1'): 'q2',
    ('q1', '2'): 'q2',
    ('q1', '3'): 'q2',
    ('q1', '4'): 'q2',
    ('q1', '5'): 'q2',
    ('q1', '6'): 'q2',
    ('q1', '7'): 'q2',
    ('q1', '8'): 'q2',
    ('q1', '9'): 'q2',
    ('q2', '0'): 'q2',
    ('q2', '1'): 'q2',
    ('q2', '2'): 'q2',
    ('q2', '3'): 'q2',
    ('q2', '4'): 'q2',
    ('q2', '5'): 'q2',
    ('q2', '6'): 'q2',
    ('q2', '7'): 'q2',
    ('q2', '8'): 'q2',
    ('q2', '9'): 'q2'
}

cadeia = input("Informe o número real: ")
print(afd(Sigma, Q, delta, 'q0', F, cadeia))

