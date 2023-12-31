def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome(input())) 

# Алгоритм проверки строки на палиндром реализован с использованием среза. Функция `is_palindrome` принимает строку `s` и сравнивает ее с обратной строкой, которая получается с помощью среза `s[::-1]`. Если строки равны, то функция возвращает `True`, в противном случае - `False`.
