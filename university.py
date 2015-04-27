class Person:
    def __init__(self):
        self.name = str(input('What is this persons name?:'))

        my_gender = str(input('What is this persons gender, M or F:'))
        if my_gender == "M" or "F":
            self.gender= my_gender
        else:
            raise ValueError('You did not enter M or F, try again.')
            my_gender()
        try:
            person_age = int(input('What is this persons age?:'))
        except ValueError:
            raise RuntimeError('You did not enter an integer')

class Student(Person):
    def __init__(self):
        Person.__init__(self)

    def enter_classes(self):
        self.class_list = []
        for i in range(1,5):
            myin = input('What is your %d class?: ' % i)
            self.class_list.append(myin)
        print(self.class_list)




Alex = Student()
Alex.enter_classes()