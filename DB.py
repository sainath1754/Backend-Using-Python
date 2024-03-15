import pymongo
def Register(collection,data):
    email = data["email"]
    try:
        existing_document = collection.find_one({"email": email})
        if existing_document:
            print("Duplicate email found:", email)
        else:
            result = collection.insert_one(data)
            print("Data inserted successfully:", result.inserted_id)
    except Exception as e:
        print(e)

def Login(collection,data):
    email = data["email"]
    password = data["password"]
    try:
        existing_document = collection.find_one({"email": email,"password":password})
        if existing_document:
            print("Your Login is Sucessfull....")
            exit()
        else:
            print("Invalid Credentials entered....")
    except Exception as e:
        print(e)







client = pymongo.MongoClient("mongodb://localhost:27017")
db_name = "Ecom_DB"
db = client[db_name]
collection = db["user_data"]
print("Database connected.....")
while True:
    print("Menu:\n1. Register\n2. Login\n3. Exit")
    ch = int(input("Enter your choice: "))
    if ch==1:
        email = input("enter your email: ")
        password1 = input("enter your password: ")
        password2 = input("re-enter your password: ")
        if password1 == password2:
            Register(collection, {"email": email, "password": password1})
        else:
            print("entered passwords do not matched......")
    elif ch==2:
        email = input("enter your email: ")
        password = input("enter your password: ")
        Login(collection,{"email": email, "password": password})
    elif ch==3:
        print("You have exited successfully.....")
        exit()
    else:
        print("enter a valid operation number....")


client.close()




