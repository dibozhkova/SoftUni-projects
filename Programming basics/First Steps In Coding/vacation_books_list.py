number_of_pages = int(input())
pages_in_1hour = int(input())
days = int(input())
time_for_1book = number_of_pages // pages_in_1hour
hours_per_day = time_for_1book // days
print(hours_per_day)