import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import uvicorn
from mutation import Mutation
from query import Query


schema = strawberry.Schema(query=Query, mutation=Mutation)


graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
