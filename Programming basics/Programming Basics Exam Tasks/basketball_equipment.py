year_taks = int(input())
# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
sneakers = year_taks - year_taks * 0.4
team = sneakers - sneakers * 0.2
ball = team * 1 / 4
accessories = ball * 1 / 5
total_sum = year_taks + sneakers + team + ball + accessories
print(f"{total_sum:.2f}")
