import factory
from django.contrib.auth import get_user_model
from factory import django
from accounts.enums import AccountTypes
from recruitment.models import University


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ('username',)

    account_type = AccountTypes.STUDENT

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    is_staff = False
    is_superuser = False

    factory.PostGenerationMethodCall('set_password', 'password123')


class UniversityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = University

    name = factory.Faker('name')
    owner = factory.SubFactory(UserFactory)
    address = factory.Faker('address')

    @factory.post_generation
    def confirmed_students(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for student in extracted:
                self.confirmed_students.add(student)
        else:
            default_students = UserFactory.create_batch(3)
            self.confirmed_students.add(*default_students)
