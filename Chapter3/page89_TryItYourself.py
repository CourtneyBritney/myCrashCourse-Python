#3-4


guest = ['Arlene', 'Zoe', 'Tazzy', 'Sally']
message = f"You are invited to dinner {guest[0].title()}."
print(message)

message = f"You are invited to dinner {guest[1].title()}."
print(message)

message = f"You are invited to dinner {guest[2].title()}."
print(message)

message = f"You are invited to dinner {guest[3].title()}."
print(message)



#3-5


print(f"{guest[0]} cannot make the dinner.")

del guest[0]
print(guest)

guest.insert(0, 'Amy')
print(guest)

message = f"You are invited to dinner {guest[0].title()}."
print(message)

message = f"You are invited to dinner {guest[1].title()}."
print(message)

message = f"You are invited to dinner {guest[2].title()}."
print(message)

message = f"You are invited to dinner {guest[3].title()}."
print(message)


#3-6


print(f"{guest[0]} I found a bigger dinner table.")

print(f"{guest[1]} I found a bigger dinner table.")

print(f"{guest[2]} I found a bigger dinner table.")

print(f"{guest[3]} I found a bigger dinner table.")

guest.append('Ruben')
print(guest)

guest.insert(0, 'Tony')
print(guest)

guest.insert(3, 'Cody')
print(guest)

message = f"You are invited to dinner {guest[0].title()}."
print(message)

message = f"You are invited to dinner {guest[1].title()}."
print(message)

message = f"You are invited to dinner {guest[2].title()}."
print(message)

message = f"You are invited to dinner {guest[3].title()}."
print(message)

message = f"You are invited to dinner {guest[4].title()}."
print(message)

message = f"You are invited to dinner {guest[5].title()}."
print(message)

message = f"You are invited to dinner {guest[6].title()}."
print(message)


#3-7


print("We can only invite two people for dinner.")

print(guest)

popped_guest1 = guest.pop()
print(f"Sorry {popped_guest1}, you are no longer invited for dinner")


popped_guest2 = guest.pop()
print(f"Sorry {popped_guest2}, you are no longer invited for dinner")


popped_guest3 = guest.pop()
print(f"Sorry {popped_guest3}, you are no longer invited for dinner")

print(guest)

popped_guest4 = guest.pop()
print(f"Sorry {popped_guest4}, you are no longer invited for dinner")

popped_guest5 = guest.pop()
print(f"Sorry {popped_guest5}, you are no longer invited for dinner")

print(guest)

message = f"You are still invited to dinner {guest[0].title()}."
print(message)

message = f"You are still invited to dinner {guest[1].title()}."
print(message)

del guest[0]
print(guest)

del guest[0]
print(guest)
