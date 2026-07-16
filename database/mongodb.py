from pymongo import MongoClient
import certifi

try:
    mongo_URI="mongodb+srv://nandinimehrasecond_db_user:nandini123@cluster0.sey86v4.mongodb.net/?appName=Cluster0"

    #TLS and certifi CA bundle
    client = MongoClient(
        mongo_URI,
        tls=True,
        tlsCAFile=certifi.where()
    )

    #test connection
    client.admin.command("ping")

    db= client["ssus"]

    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_reports"]

    print("MongoDB Connected Successfully")

except Exception as e:
    print("mongodb error:",e)    