# You are a mad scientist, and you have decided to play with electron distribution among atom shells. The basic idea of electron distribution is that electrons should fill a shell until it holds the maximum number of electrons.
# You will receive a single integer - the number of electrons. Your task is to fill shells until there are no more electrons left. The rules for electron distribution are as follows:
# •	The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1). For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
# •	You should start filling the shells from the first one at the first position.
# •	If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and so on.
# In the end, print a list with the filled shells.


number_of_electrons = int(input())
shell_list = []
index = 0
while 0 < number_of_electrons:
    index += 1
    shell = 2 * index ** 2
    if number_of_electrons >= shell:
        shell_list.append(shell)
        number_of_electrons -= shell
    else:
        shell_list.append(number_of_electrons)
        number_of_electrons = 0
print(shell_list)
