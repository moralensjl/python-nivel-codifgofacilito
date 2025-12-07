
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


user1 = User('Cody', '1234', 'cody@codicofacilito.com')
print(user1.username)
print(user1.password)
print(user1.email)

