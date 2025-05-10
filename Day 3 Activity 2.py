Amount= int(input('number:'))

note_100 = Amount//100
note_50 = (Amount%100)//50
note_10 = ((Amount%100)%50)//10

print(note_100)
print(note_50)
print(note_10)