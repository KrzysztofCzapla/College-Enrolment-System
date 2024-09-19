from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType

from recruitment.models import University
User = get_user_model()

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("username", "email", "account_type")


class UniversityType(DjangoObjectType):
    class Meta:
        model = University
        fields = ("name", "owner", "address", "confirmed_students")


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_universities = graphene.List(UniversityType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    university_by_id = graphene.Field(UniversityType, id=graphene.Int(required=True))

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_universities(root, info):
        return University.objects.select_related('owner').prefetch_related("confirmed_students").all()

    def resolve_user_by_id(root, info, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None

    def resolve_university_by_id(root, info, id):
        try:
            return University.objects.select_related('owner').prefetch_related("confirmed_students").get(pk=id)
        except University.DoesNotExist:
            return None


class CreateUniversity(graphene.Mutation):
    university = graphene.Field(UniversityType)

    class Arguments:
        name = graphene.String(required=True)
        address = graphene.String()
        owner_id = graphene.Int(required=True)
        confirmed_students_ids = graphene.List(graphene.Int)

    def mutate(root, info, name, address, owner_id, confirmed_students_ids):
        try:
            owner = User.objects.get(pk=owner_id)
        except User.DoesNotExist:
            raise Exception("Owner not found")
        try:
            confirmed_students = User.objects.filter(id__in=confirmed_students_ids)
        except User.DoesNotExist:
            raise Exception("Owner not found")

        university = University(name=name, address=address, owner=owner, confirmed_students=confirmed_students)
        university.save()
        return CreateUniversity(university=university)


class Mutation(graphene.ObjectType):
    create_university = CreateUniversity.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
