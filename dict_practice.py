#Total sales for each type of produce over the past 3 weeks
#Average sales per week for each type of produce
#Percentage change in sales for each type of produce from the previous week to the current week
#Combine the data into a new dictionary and print the results
#print the declining sales
#print the rising sales 
#lets write a report that gives us an overview of the best sellers, the worst sellers, 
    #and the average volume. Lets add the bottom and top total sales performers as well. 

import os
import random
    
#randomly generated sales volume of a produce section at grocery store   
grocery_dict = {
    "apple": [random.randint(1,500),random.randint(1,500), random.randint(1,500)],
    "banana": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "orange": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "kiwi": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "lemon": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "lime": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "grapefruit": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "mango": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "pineapple": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "pear": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "peach": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "plum": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "watermelon": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "cantaloupe": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "honeydew": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "strawberry": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "blueberry": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "raspberry": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "blackberry": [random.randint(0,500),random.randint(0,500), random.randint(0,500)],
    "grape": [random.randint(0,500),random.randint(0,500), random.randint(0,500)]
}
# Sales data storage area
tsd = {} #total sales volume
asd = {} # average sales volume
csd = {} # percentage change in sales volume
fsd = {} # products with falling sales volume
rsd = {} # products with rising sales volume
top_ten = {} # top 10% performers
bottom_ten = {} # bottom 10% performers 
ctop = {} #top % movers
cbottom = {}#bottom % movers


#sum the sales volume
for key, value in grocery_dict.items():
    total_sales = sum(value)
    tsd[key] = total_sales
#print the total sales
#for key, value in tsd.items():
    #print(key, ":", value)

#calculate average sales volum
for key, value in grocery_dict.items():
    average_sales = sum(value)/3
    asd[key] = average_sales
#print the average sales volume
#for key, value in asd.items():
    #print(key, " ", value)

#calculate change in sales volume
for key, value in grocery_dict.items():
    change = (value[1] - value[0])/value[0]
    csd[key] = change
#print the change in sales volume 
#for key, value in csd.items():
    #print(key, " ", value)

#combine the data into a dictionary  
sales_data = {key: (tsd[key], asd[key], csd[key]) for key in grocery_dict}
#print the combined dictionary 
#for key, total in sales_data.items():
    #print(key," ", total)

# find the items with falling sales 
for key, value in csd.items():
    if value < 0:
        fsd[key] = value

#print falling sales
#for key, value in fsd.items():
    #print(key, " ", value)

# find the items with rising sales 
for key, value in csd.items():
    if value > 0:
        rsd[key] = value

#print rising sales
#for key, value in rsd.items():
    #print(key, " ", value)

#find the top preformers of total sales
values = [item[1] for item in tsd.items()]
values.sort(reverse=True)
top10 = values[:int(len(values)*.1)]
bottom10 = values[-int(len(values)*.1):]

#Match value to key in total sales dictionary 
for key, value in tsd.items():
    if value in top10:
        top_ten[key] = value
for key, value in tsd.items():
    if value in bottom10:
        bottom_ten[key] = value

#find the top percentage movers
cvalues = [item[1] for item in csd.items()]
cvalues.sort(reverse=True)
ctop10 = cvalues[:int(len(values)*.1)]
cbottom10 = cvalues[-int(len(values)*.1):]

#Match value to key in CSD
for key, value in csd.items():
    if value in ctop10:
        ctop[key] = value
for key, value in csd.items():
    if value in cbottom10:
        cbottom[key] = value

# find out what the total sales volume is in 'units' for this week
week_total = sum([value[2] for value in grocery_dict.values()])
last_total = sum([value[1] for value in grocery_dict.values()])

volume_change = (week_total - last_total)/last_total

#clear the terminal 
os.system('cls' if os.name == 'nt' else 'clear')

#Report
print("This week we sold: " + str(week_total) + " fruit units.")
print("A " + str(volume_change) + " change from last week.")
print("Our top sellers are: ")
print(top_ten)
print("Our bottom sellers are: ")
print(bottom_ten)
print("Products with the largest volume increases are: ")
print(ctop)
print("Products with the largest volume DECREASES are: ")
print(cbottom)