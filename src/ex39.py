# creating and accessing lists

states = {
        'Oregon':'OR',
        'Florida':'FL',
        'California':'CA',
        'New York':'NY',
        'Michigan':'MI'
        }

cities = {
        'CA':'San Francisco',
        'MI':'Detroit',
        'FL':'Jacksonville'
        }

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-'*10)
print("NY State has: ",cities['NY'])
print("OR State has: ",cities['OR'])

print('-'*10)
print("Michigan's abbrev is: ",states['Michigan'])
print("Florida's abbrev is: ",states['Florida'])

print('-'*10)
print("Michigan has: ",cities[states['Michigan']])
print("Florida has: ",cities[states['Florida']])

print('-'*10)
for state , abbrev in list(states.items()):
    print(states,' ',abbrev)

for abbrev , city in list(cities.items()):
    print(abbrev , ' ' , city)

for state , abbrev in list(states.items()):
    print(state, ': ',abbrev,': ',cities[abbrev])

state = states.get('Texas')

if not state:
    print("Sorry,no Texas")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
