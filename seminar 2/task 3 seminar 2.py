s = input()
palindrome = s[::-1] == s
mirror_dict = {'A': 'A',
               'H': 'H',
               'I': 'I',
               'M': 'M',
               'O': 'O',
               'T': 'T',
               'U': 'U',
               'V': 'V',
               'W': 'W',
               'X': 'X',
               'Y': 'Y',
               '1': '1',
               '8': '8',
               'E': '3',
               '3': 'E',
               'J': 'L',
               'L': 'J',
               'S': '2',
               '2': 'S',
               'Z': '5',
               '5': 'Z'}
mirror_s = ''
for character in s:
    if character not in mirror_dict:
        break
    mirror_s += mirror_dict[character]
mirrored = mirror_s[::-1] == s
if mirrored and palindrome:
    print(s + ' is a mirrored palindrome.')
elif mirrored:
    print(s + ' is a mirrored string.')
elif palindrome:
    print(s + ' is a regular palindrome.')
else:
    print(s + ' is not a palindrome.')