# Kostka_do_gry

Funkcję, przyjmuje w parametrze kod w postaci łańcucha znaków, rozpoznaje dane wejściowe:
typ kostki (D3, D4, D6, D8, D10, D12, D20, D100), liczbę rzutów i modyfikator. Kod kostki to: xDy+z gdzie: 
y – rodzaj kostek, których należy użyć (np. D6, D10),
x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).
Jeżeli podany ciąg znaków jest niepoprawny, zwraca odpowiedni komunikat. 
Jeżeli jest poprawny wykonuje symulację rzutów i zwraca wynik.
