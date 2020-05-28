#9-12

from admin import Admin

courtney = Admin('courtney', 'alexander', 'c_alexander', 'courtney13alexander@gmail.com', 'eldorado park')
courtney.describe_user()

courtney_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
courtney.privileges.privileges = courtney_privileges

print(f"\nThe admin {courtney.username} has these privileges: ")
courtney.privileges.show_privileges()