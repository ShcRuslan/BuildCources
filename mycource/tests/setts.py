from ..models import Category, Course, Branch, Contact


def create_category(name='Programming', imgpath='programmingPicture'):
    return Category.objects.create(name=name, imgpath=imgpath)


def create_course(name='Neobis', description='bla bla bla', category=None, logo='some logo'):
    return Course.objects.create(name=name, description=description, category=category, logo=logo)


def create_branch(latitude='454545', longitude='555555', address='Tinistanov St.', course=None):
    return Branch.objects.create(latitude=latitude, longitude=longitude, address=address, course=course)


def create_contact(type= 1, value= 'value', course=None):
    return Contact.objects.create(type=type, value=value, course=course)