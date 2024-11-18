def add_dollars_and_cents(d1, c1, d2, c2):
    total_cents = c1 + c2
    total_dollars = d1 + d2
    if total_cents >= 100:
        total_dollars += total_cents // 100  
        total_cents = total_cents % 100     
    print(total_dollars)
    print(total_cents)

d1 = int(input())  
c1 = int(input())  
d2 = int(input())  
c2 = int(input())  


add_dollars_and_cents(d1, c1, d2, c2)
