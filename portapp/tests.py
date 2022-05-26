from django.test import TestCase
from .models import Person, Project

# Create your tests here.
class PersonTestClass(TestCase):

    # Set up method ---test class for the person module
    def setUp(self):
        self.reuben= Person(first_name = 'Reuben', last_name ='Rotich')
        
    #creates an instance of our person class---||is the object being created well or being instantiated well
    def test_instance(self):
        self.assertTrue(isinstance(self.reuben,Person))
        
    #How we can save our person
    def test_save_method(self):
        self.reuben.save_person()
        user_persons = Person.objects.all() #querying all our persons
        self.assertTrue(len(user_persons) > 0)
    
    
    #Try and have a delete function
    def test_delete_method(self):
        self.reuben.delete_person()
        user_persons = Person.objects.all()
        self.assertTrue(len(user_persons),1)
        

#Projects tests
class ProjectTestClass(TestCase):
    def setUp(self):
        self.reuben =Person(first_name = 'Reuben', last_name ='Rotich')
        self.reuben.save()
        
    def setUp(self):
        self.new_project = Project(name = "Portfolio", description="my braggable projects", person=self.reuben)
        
        self.new_project.save()
        
        
    def tearDown(self):
        Person.objects.all().delete()
        Project.objects.all().delete()