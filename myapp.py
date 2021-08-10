from api import app
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType, QueryType, SubscriptionType
from ariadne.constants import PLAYGROUND_HTML
from ariadne.asgi import GraphQL
from flask import request, jsonify
from api.queries import listSensors_resolver, bySensorsId_resolver
from api.mutations import createSensors_resolver
from api.subscriptions import sensorMessages_source, sensorMessages_resolver

query = QueryType()
mutation = ObjectType("Mutation")
subscription = SubscriptionType()

query.set_field("listSensorID", listSensors_resolver)
query.set_field("getSensorID", bySensorsId_resolver)
mutation.set_field("createSensor",createSensors_resolver)
subscription.set_source("messageSensor", sensorMessages_source)
subscription.set_field("messageSensor", sensorMessages_resolver)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query, mutation, subscription ,snake_case_fallback_resolvers)
application = GraphQL(schema)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code