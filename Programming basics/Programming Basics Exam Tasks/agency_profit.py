air_line = input()
num_ticket_adults = int(input())
num_ticket_children = int(input())
price_ticket_adult_net = float(input())
service_tax = float(input())

price_ticket_children_net = price_ticket_adult_net - (price_ticket_adult_net * 0.7)
total_price_ticket_adult = price_ticket_adult_net + service_tax
total_price_ticket_children = price_ticket_children_net + service_tax
total_sum_all_tickets = num_ticket_adults * total_price_ticket_adult + num_ticket_children * total_price_ticket_children
profit_agency = total_sum_all_tickets * 0.2
print(f"The profit of your agency from {air_line} tickets is {profit_agency:.2f} lv.")
