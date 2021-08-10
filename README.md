This guideline will helps you set up the python service to stream datafrom influxdb over graphql. 

### Pre-requisite:
* Create the account on cloud influxdb  https://us-east-1-1.aws.cloud2.influxdata.com
* Install influxdb client (pip install influxdb_client)
* Install  ariadnea which is a Python library for implementing GraphQL servers using schema-first approach. (pip install ariadne)
* If you want to implement Queries and Mutation you can install flask server **pip install flask**(If you want to implement subscription as well you need a ASGI server).
* For subscriptions you need to install **uvicorn** an asgi server. We install uvicorn with the “standard” option since that brings optional extras like WebSocket support which is needed for subscription. **pip install ariadne "uvicorn[standard]"**

### Steps
* Pull the Project https://git-ce.rwth-aachen.de/iop/infrastructure/Graphql-Python-Influxdb
* load the data which is present in folder demo-data if you want to play with the demo data. Otherwise load your own data in your cloud influxdb.
* In model.py replace **token, org and bucket** variable to your influxdb credentials.
* In model.py we have define 2 function which helps to get data for two different resolvers. you can reuse it or can create your own query depending in your requirement.
* In schema.graphql you can define your schema and all the type of queries. (for more detail  https://dgraph.io/blog/post/designing-graphql-schemas/)
* In queries.py define all your resolvers. for e.g. we have define two resolver one which return all sensors data (listsensors_resolvers) and other one is which return data of a particular sensor id(bysensorid_resolver)
* In myapp.py import all your resolvers. for e.g (from api.queries import listSensors_resolver, bySensorsId_resolver)
* In myapp.py set all your resolver. For e.g. (query.set_field("listSensorID", listSensors_resolver))
* Run the application by typing **uvicorn myapp:application --reload** or **flask run** in CLI.
* Go to studio.apollographql.com/dev and create an account (using either GitHub or your email). Choose a name for our graph, and select the development option as the graph type.
* Add our localhost endpoint http://localhost:Port/graphql in the endpoint field and click create graph.
* Note: If you are using flask port would be 5000 and if you are using uvicorn port would be 8000
* Once the setup is done, we will see that the GraphQL IDE will load up in our browser.


### Reading Links
* https://www.apollographql.com/blog/graphql/python/complete-api-guide/
* https://www.influxdata.com/blog/using-graphql-with-influxdb-and-flux/
* https://wahlnetwork.com/2020/08/04/how-to-query-graphql-apis-with-python/
* https://ariadnegraphql.org/docs/subscriptions.html
* https://www.twilio.com/blog/graphql-api-subscriptions-python-asyncio-ariadne
