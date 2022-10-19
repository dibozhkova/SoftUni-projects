# You will receive a number representing the number of wagons a train has. Create a list (train) with the given length containing only zeros. 
# Until you receive the command "End", you will receive some of the following commands:
# •	"add {people}" – you should add the number of people in the last wagon
# •	"insert {index} {people}" - you should add the number of people at the given wagon
# •	"leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.


number_of_wagons = int(input())
wagons = [0] * number_of_wagons
command = input()
while command != "End":
    data = command.split()
    if data[0] == "add":
        wagons[-1] += int(data[1])
    elif data[0] == "insert":
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] += int(number_of_people)
    elif data[0] == "leave":
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] -= int(number_of_people)
    command = input()
print(wagons)
