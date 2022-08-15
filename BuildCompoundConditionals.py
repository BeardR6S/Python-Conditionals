username = 'jonsnow' #change user to anything else it will kick back with the else statement.
email = 'jon@snow.com'
password = 'thenorth'

#both the left of AND and the right have to be true to work.

if username == 'jonsnow' and password == 'thenorth': #can swap 'and' for 'or' operator but just needs ONE of the requirements to be permitted. Not great due to ease of access. CS would have a field day with this.
    print('Access Permitted')
else:
    print('You shall not pass!')

"""
You can do this like this as well, not recommended by instructor.

if username == 'jonsnow':
    if password == 'thenorth':
        print('Access permitted')
else:
    print('You shall not pass!')
"""

"""
if (username == 'jonsnow' or email == 'jon@snow.com) and password == 'thenorth': 
    print('Access Permitted')
else:
    print('You shall not pass!') 

^Would be best for log in page with either email or username input^ requires one of the left side and the right side input to be right to get access
"""

"""
logged_in = True
standard_user = True

if logged_in and not standard_user:
    print('You can access the Admin Dashboard')
else:
    print('You can only access the standard dashboard') 
    
^left hand side needs to be true, left hand side needs to be false for it to work.^
"""