def palindrome(s):
    return s[::-1] == s
while True:
    s = input("Введите слово: ")
    print (f" True"
           if palindrome(s) else f" False ") 


