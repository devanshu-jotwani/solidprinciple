from abc import ABC, abstractmethod

class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass

class PersonDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')

class PersonXML(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')

if __name__ == '__main__':
    person = Person('John Doe')
    storage = PersonXML()
    storage.save(person)
    
