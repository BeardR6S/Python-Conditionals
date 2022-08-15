role = 'Admin'

auth = 'can access' if role == 'Admin' else 'cannot access'

print(auth) #this and everything above it == ternary operator

# if role == 'Admin':
#     auth = 'can access'
# else:
#     auth = 'cannon access'

# print(auth)