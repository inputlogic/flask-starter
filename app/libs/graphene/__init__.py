import graphene
from flask_graphql import GraphQLView

from .user import User as UserType, CreateUser
from app.models.user import User


class Query(graphene.ObjectType):
    hello = graphene.String()
    user = graphene.Field(UserType, email=graphene.String())

    def resolve_hello(self, args, context, info):
        return 'World'

    def resolve_user(self, args, context, info):
        email = args.get('email')
        return User.objects(email=email).first()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


def load(app):
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )
