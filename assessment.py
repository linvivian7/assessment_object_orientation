"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   i) Polymorphism: The ability to perform operations on instances across
      classes without specifying conditionals. This is especially helpful
      for parent and child classes with methods that share a name but
      have different implementation within each class.

   ii) Abstraction: The ability to "hide" the inner-workings of a class
       and its methods. This is helpful to reduce the inadvertent manipulation
       of methods, class variables, etc. by users. Abstraction is the
       demonstration of the principle that an individual does not need to know
       how something works, but just that it does.

   iii) Encapsulation: The ability to group all items (e.g. variables,
        attributes, methods, etc.) relevant to the class together. This is
        helpful for isolating classes in order to debug. Encapsulation also
        contains attribute manipulation within the specified class so that
        inadvertent manipulation can be minimized.

2. What is a class?

    A class can be built-in within the programming language (e.g. file,
    exception, list, str) or user-defined objects. A class with an __init__
    method allows for instantiation of the class and instances of each
    class are defined by common parameters that are either defined at
    the class or instance level, or are passed in explicitly. Classes are
    more organizable compared to other data structures and user-defined
    classes are recognized by Python as a "type". This makes it a powerful
    tool for programmers.

3. What is an instance attribute?

    An instance attribute is a trait that is "given" to that instance and
    can be all types of parameters. An attribute is called by the "." that
    follows the instance name. As mentioned above, instance attributes
    can be given within the __init__ method when instantiated or explicitly
    passed.

4. What is a method?

    A method is a function that is defined within a class. There are
    generally two types of methods. 1) Dunder methods just as __repr__
    and __init__ are important, complementary methods that are not meant to
    be called directly by the user. Dunder methods are critical to defining
    instances and how they are representated. 2) Non-dunder methods perform
    everything functions can, but are now class-specific (or in some cases,
    parent/child class hierarchy specific). They are meant to be called
    with a ".()" following an instance.

5. What is an instance in object orientation?

    An instance is an event/occurence/example of a class (e.g. scottish_fold
    is an instance of class CuteCat). They are instantiated when the instance
    name is assigned to a class and satisfies all arguments the class __init__
    method requires.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Typically, a class attribute is defined for all instances within the class
   and is not expected to change. An instance attribute is expected to vary
   between different instances. For example, class Undergrad at Someschool
   might have a class attribute (school = Someschool) and instance attributes
   self.class_level, self.dorm_status, self.GPA, etc.) A caveat of class
   attributes is that, once instantiated, the attribute of an instance can be
   overridden by assigning a instance attribute of the same name.

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """ Student information """

    def __init__(self, first_name, last_name, address):
        """ Instantiates with instance variables """

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """ Question and its correct answer """

    def __init__(self, question, correct_answer):
        """ Instantiate with instance variables """

        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        return "{}".format(self.question)

    def ask_and_evaluate(self):
        """ Return True or False based on correct answer """

        user_answer = raw_input("Q:{}\nA:".format(self.question))
        return user_answer == self.correct_answer


class Exam(object):
    """ Exam with questions """

    # Initializes number of question on each exam
    question_counter = 0

    def __init__(self, name):
        """ Instantiate with instance variables """

        self.name = name
        self.questions = []  # list items are Question objects

    def __repr__(self):
        return self.name

    def add_question(self, question, correct_answer):
        """ Add instantiated Question to test """

        self.question_counter += 1
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        """ Grade test question by question, return percent score """

        self.score = 0

        # Loop through each question added to test
        # Call method from Question class
        for question in self.questions:
            if question.ask_and_evaluate() is True:
                self.score += 1

        # Convert raw score to percentage
        percent_score = round(self.score * 100 / len(self.questions), 1)
        return percent_score


def take_test(exam_name, student):
    """ Print student percentage test score """

    student.score = exam_name.administer()
    print "{} scored {}% on this {}.".format(student.first_name, student.score, exam_name)


def example():
    """ Initialize exam and student, grade exam, and assign score variable to student """

    new_test = Exam("test of courage")
    new_test.add_question("Which chemical element has the symbol Sb?", "Antimony")
    new_test.add_question("For centuries these were thought to “tenderize” meat. In 1845 it was discovered that they were poisonous.", "maggots")
    new_test.add_question("62% of people claim they know how to do this even though they have never actually done it by themselves", "change a flat tire")
    fake_student = Student("Glasses", "Potter", "Castlelookingplace")
    take_test(new_test, fake_student)


class Quiz(Exam):
    """ Quiz with questions """

    def administer(self):
        count = 0

        for question in self.questions:
            if question.ask_and_evaluate() is True:
                count += 1

        return count > .5 * (len(self.questions))


def take_quiz(quiz_name, student):
    """ Print student quiz pass/fail status """

    if quiz_name.administer() is True:
        student.quiz_score = "passed"
    else:
        student.quiz_score = "failed"
    print "{} {} this {}.".format(student.first_name, student.quiz_score, quiz_name)


def example_quiz():
    """ Initialize exam and student, grade exam, and assign score variable to student """

    new_quiz = Quiz("quiz of happiness")
    new_quiz.add_question("what's the capital of meow?", "I don't meow")
    new_quiz.add_question("What's up dog?", "what??")
    new_quiz.add_question("What is a cation afraid of?", "dogion")
    real_student = Student("Meowy", "Smith", "Poolside")
    take_quiz(new_quiz, real_student)



























