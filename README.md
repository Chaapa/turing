# turing

Эмулятор машины Тьюринга

Пример программы на ввод:
q1 0 q4 0 R \\
q1 1 q2 0 R
q2 1 q2 1 R
q2 0 q3 0 R
q3 0 q4 1 R
q4 0 q5 1 R
q5 0 q6 1 L
q6 0 q7 0 L
q6 1 q6 1 L
q7 0 q1 0 R
q7 1 q7 1 L
q3 1 q3 1 R
q4 1 q8 0 R
q8 1 q0 0 S
end

Обязательно сотояние должно описываться как qi, где i любая подстрока. Заканчиваться программа должна словом end

