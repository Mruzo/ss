import graphene
import sharespace.schema


class Query(sharespace.schema.Query, graphene.ObjectType):
    #This class will inherit from multiple Queries as we begin to add more apps to our project
    pass


class Mutation(sharespace.schema.Mutation, graphene.ObjectType):
    #This class will inherit from multiple Queries as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
