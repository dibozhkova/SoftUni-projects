movie = input()
student_all = 0
standard_all = 0
kid_all = 0
tickets_total = 0

while movie != "Finish":
    current_free_spaces = int(input())
    type_ticket = input()
    all_tickets = 0

    while type_ticket != "End":
        all_tickets += 1
        tickets_total += 1
        if type_ticket == "student":
            student_all += 1
        elif type_ticket == "standard":
            standard_all += 1
        elif type_ticket == "kid":
            kid_all += 1
        if all_tickets == current_free_spaces:
            break
        type_ticket = input()
    percent_capacity = (all_tickets / current_free_spaces) * 100
    print(f"{movie} - {percent_capacity:.2f}% full.")
    movie = input()
print(f"Total tickets: {tickets_total}")
percent_student = student_all / tickets_total * 100
print(f"{percent_student:.2f}% student tickets.")
print(f"{standard_all / tickets_total * 100:.2f}% standard tickets.")
print(f"{kid_all / tickets_total * 100:.2f}% kids tickets.")
