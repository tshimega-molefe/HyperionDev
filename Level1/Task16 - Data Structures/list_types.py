# This programme will help us store the names of three of my friends in my friend list.

max_friends = 3
friends_names = []
friends_ages = []


while len(friends_names) < max_friends and len(friends_ages) < max_friends:
    friend = input("Enter your friend's full name: ")
    friend_age = int(input("Enter your friend's age: "))
    friends_names.append(friend)
    friends_ages.append(friend_age)
    print(f"You added {friend} as a friend. They're {friend_age} years old.")

print(
    f"Friend list is full. Here are your friends and their respective ages: {friends_names}, {friends_ages}. Your friend list has {len(friends_names)} people in it.\nYour first friend's name is {friends_names[0]}, and your last friend's name is {friends_names[-1]}."
)
