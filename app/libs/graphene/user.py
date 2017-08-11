import graphene
from app.models.user import User as UserModel


class User(graphene.ObjectType):
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    id = graphene.String()

    def resolve_id(self, args, context, info):
        return str(self.id)


class CreateUserInput(graphene.InputObjectType):
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    password = graphene.String()


class CreateUser(graphene.Mutation):
    class Input:
        input = graphene.Argument(CreateUserInput)

    ok = graphene.Boolean()
    user = graphene.Field(User)

    @staticmethod
    def mutate(root, args, context, info):
        user = UserModel.register(**args['input'])
        user = User(
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name
        )
        ok = True
        return CreateUser(user=user, ok=ok)
