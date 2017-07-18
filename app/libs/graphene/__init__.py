import graphene
from flask_graphql import GraphQLView


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, args, context, info):
        return 'World'


schema = graphene.Schema(query=Query)


def load(app):
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )
