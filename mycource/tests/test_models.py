from django.test import TestCase

from mycource.models import Category, Course, Branch, Contact
from mycource.tests.setts import create_category, create_course, create_branch, create_contact


class CategoryModelTest(TestCase):

    def test_category_create(self):
        cat = create_category()
        self.assertTrue(isinstance(cat, Category))
        self.assertTrue(str(cat), cat.name)

    def setUp(self):
        Category.objects.create(name='Programming', imgpath='programmingPicture')

    def test_category_name(self):
        category = Category.objects.get(id=1)
        example = category._meta.get_field('name').verbose_name
        self.assertEquals(example, 'name')

    def test_category_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)


class CourseModelTest(TestCase):

    def test_course_create(self):
        cour = create_course()
        self.assertTrue(isinstance(cour, Course))
        self.assertTrue(str(cour), cour.name)

    def setUp(self):
        cat = Category.objects.create(name='Programming', imgpath='programmingPicture')
        Course.objects.create(name='Neobis', description='bla bla bla', category=cat, logo='some logo')

    def test_course_name(self):
        course = Course.objects.get(id=1)
        example = course._meta.get_field('name').verbose_name
        self.assertEquals(example, 'name')

    def test_course_name_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_course_description(self):
        course = Course.objects.get(id=1)
        example = course._meta.get_field('description').verbose_name
        self.assertEquals(example, 'description')

    def test_course_category(self):
        course = Course.objects.get(id=1)
        example = course._meta.get_field('category').verbose_name
        self.assertEquals(example, 'category')

    def test_category_logo(self):
        course = Course.objects.get(id=1)
        example = course._meta.get_field('logo').verbose_name
        self.assertEquals(example, 'logo')

    def test_course_logo_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('logo').max_length
        self.assertEquals(max_length, 100)


class BranchModelTest(TestCase):

    def test_branch_create(self):
        branch = create_branch()
        self.assertTrue(isinstance(branch, Branch))
        self.assertTrue(str(branch), branch.address)

    def setUp(self):
        cat = Category.objects.create(name='Programming', imgpath='programmingPicture')
        course = Course.objects.create(name='Neobis', description='bla bla bla', category=cat, logo='some logo')
        Branch.objects.create(latitude='454545', longitude='555555', address='Tinistanov St.', course=course)

    def test_branch_latitude(self):
        branch = Branch.objects.get(id=1)
        example = branch._meta.get_field('latitude').verbose_name
        self.assertEquals(example, 'latitude')

    def test_branch_latitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('latitude').max_length
        self.assertEquals(max_length, 100)

    def test_branch_longitude(self):
        branch = Branch.objects.get(id=1)
        example = branch._meta.get_field('longitude').verbose_name
        self.assertEquals(example, 'longitude')

    def test_branch_longitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('longitude').max_length
        self.assertEquals(max_length, 100)

    def test_branch_course(self):
        branch = Branch.objects.get(id=1)
        example = branch._meta.get_field('course').verbose_name
        self.assertEquals(example, 'course')

    def test_branch_address(self):
        branch = Branch.objects.get(id=1)
        example = branch._meta.get_field('address').verbose_name
        self.assertEquals(example, 'address')

    def test_branch_address_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('address').max_length
        self.assertEquals(max_length, 100)


class ContactModelTest(TestCase):

    def test_course_create(self):
        contact = create_contact()
        self.assertTrue(isinstance(contact, Contact))
        self.assertTrue(str(contact), contact.value)

    def setUp(self):
        course = Course.objects.create(name='Neobis', description='bla bla bla', category=None, logo='some logo')
        Contact.objects.create(type=1, value='value', course=course)

    def test_contact_type(self):
        contact = Contact.objects.get(id=1)
        example = contact._meta.get_field('type').verbose_name
        self.assertEquals(example, 'type')

    def test_contact_value(self):
        contact = Contact.objects.get(id=1)
        example = contact._meta.get_field('value').verbose_name
        self.assertEquals(example, 'value')

    def test_contact_value_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('value').max_length
        self.assertEquals(max_length, 100)

    def test_contact_value(self):
        contact = Contact.objects.get(id=1)
        example = contact._meta.get_field('course').verbose_name
        self.assertEquals(example, 'course')