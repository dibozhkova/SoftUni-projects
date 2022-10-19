# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}". 
# Return a list containing all to-do notes sorted by importance in ascending order. 
# The importance value will always be an integer between 1 and 10 (inclusive).


notes = [0] * 10
command = input()
while command != "End":
    current_note = command.split("-")
    priority_note = int(current_note[0]) - 1
    note = current_note[1]
    notes.pop(priority_note)
    notes.insert(priority_note, note)
    command = input()
result = ([el for el in notes if el != 0])
print(result)
