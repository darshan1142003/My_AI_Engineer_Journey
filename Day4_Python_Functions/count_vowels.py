text = input("enter text: ")

def vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            count =  count + 1
    return count
print(vowels(text))
        