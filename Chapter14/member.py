class Member:
    """A member of a university."""


    def __init__(self, name, address, email):
        """(Member, str, str, str) -> NoneType

        Create a new member named name, with home address and email address.
        """

        self.name = name
        self.address = address
        self.email = email


    def __str__(self):
        """(Member) -> str
        Return a string representation of this member.
        >>> member = Member('Paul', 'Ajax', 'pgries@cs.toronto.edu')
        >>> member.__str__()
        'Paul\\nAjax\\npgries@cs.toronto.edu'
        """
        return f'{self.name}\n{self.address}\n{self.email}'

class Faculty(Member):
    """A faculty member at a university."""


    def __init__(self, name, address, email, faculty_num):
        """(Member, str, str, str, str) -> NoneType

        Create a new faculty named name, with home address,
        email address, faculty_num, and empty list of courses.
        """

        super().__init__(name, address, email)
        self.faculty_num = faculty_num
        self.courses_teaching = []

class Student(Member):
    """A student member at a university."""


    def __init__(self, name, address, email, student_num):
        """(Member, str, str, str, str) -> NoneType

        Create a new student member named name, with home address,
        email address, student number, an empty list of courses taken,
        and an list of current courses.
        """

        super().__init__(name, address, email)
        self.student_num = student_num
        self.courses_taken = []
        self.current_courses = []

paul = Faculty('Paul Gries', 'Ajax', 'pgries@cs.toronto.edu', '1234')
print(paul)

jen = Student('Jen Campbell', 'Toronto', 'campbell@cs.toronto.edu', '4321')
print(jen.name)
