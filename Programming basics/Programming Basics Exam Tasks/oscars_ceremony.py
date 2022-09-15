rent = int(input())
# •	Статуетки  – цената им е 30% по-малка от наема на залата
# •	Кетъринг – цената му е 15% по-малка от тази на статуетките
# •	Озвучаване – цената му е 1 / 2 от цената за кетъринг
statuettes = rent - rent * 0.3
catering = statuettes - statuettes * 0.15
voicing = catering - catering * 0.5
total_cost = rent + statuettes + catering + voicing
print(f"{total_cost:.2f}")
