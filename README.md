# turing

Эмулятор машины Тьюринга

Пример программы на ввод:<br />
q1 0 q4 0 R <br />
q1 1 q2 0 R <br />
q2 1 q2 1 R <br />
q2 0 q3 0 R <br />
q3 0 q4 1 R <br />
q4 0 q5 1 R <br />
q5 0 q6 1 L <br />
q6 0 q7 0 L <br />
q6 1 q6 1 L <br />
q7 0 q1 0 R <br />
q7 1 q7 1 L <br />
q3 1 q3 1 R <br />
q4 1 q8 0 R <br />
q8 1 q0 0 S <br />
end <br />

Обязательно сотояние должно описываться как q$i$, где i любая подстрока. Заканчиваться программа должна словом end

