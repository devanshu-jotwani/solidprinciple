class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name})'


class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')


if __name__ == '__main__':
    p = Person('John Doe')
    ''' if save method was in Person then we would have to change the method and modify
        class Person which would not be a single responsibility principle
        that is why class PersonDB does the work of storing the person in database while
        class Person does initialization
    '''
    db = PersonDB()
    db.save(p)
