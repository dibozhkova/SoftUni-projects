line_input = int(input())
balanced_bracket = 0
open_bracket = 0
all_bracket = 0
for string in range(line_input):
    current_string = input()
    if current_string == "(":
        open_bracket += 1
        all_bracket += 1
    if current_string == ")":
        all_bracket += 1
    if open_bracket == 1 and current_string == ")":
        open_bracket = 0
        balanced_bracket += 1
if balanced_bracket > 0:
    if (all_bracket / balanced_bracket) % 2 == 0:
        print("BALANCED")
    else:
        print("UNBALANCED")
else:
    print("UNBALANCED")
