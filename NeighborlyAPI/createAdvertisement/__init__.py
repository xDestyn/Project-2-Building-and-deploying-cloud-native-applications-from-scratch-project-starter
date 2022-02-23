import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://proj2-cosmosdb-account01:DozOVQnyXAY72eVYeTM29Ahf5E3Eiy1RiyEbUtB3FTuTV1ODPkdVMAu9Q20R2SCvv2xteGgLWuqZ6VadkcxzCg==@proj2-cosmosdb-account01.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@proj2-cosmosdb-account01@"  
            # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['advertisementsdb']
            collection = database['AdvertisementsCollection']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )