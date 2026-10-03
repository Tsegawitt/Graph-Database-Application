# Name: Tsegawit Gebremedhin
# Date: October 2, 2026
# Assignment: Performance Assessment - Python Application Accessing a Document Database
# Purpose: Interactive menu-driven CRUD application using PyMongo to manage Amazon review documents.

import pymongo

def main():
    # Connect to the local Mongo database
    print("Connecting to local Mongo database...")
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myClient["Amazon"]
    myCollection = db["ReviewData"]
    print("Data imported successfully!\n")

    while True:
        # Main Menu options matching professor's sample images
        print("Type a number and press enter to execute the menu option.")
        print("1. Query for documents")
        print("2. Add a new document")
        print("3. Update fields of a document")
        print("4. Delete a document")
        print("5. Delete all documents from the collection")
        print("6. Delete a collection")
        print("7. Exit the program")
        
        choice = input().strip()

        # --- 1. QUERY FOR DOCUMENTS ---
        if choice == "1":
            print("\nPlease type a number and press enter to execute the menu option")
            print("1. Query by reviewID")
            print("2. Filter for a number of stars and greater")
            print("3. Filter for less than a number of stars")
            print("4. Filter for a word in the title")
            print("5. Filter for a word in the review body content")
            
            sub_choice = input().strip()

            if sub_choice == "1":
                rev_id = input("\nEnter the ReviewID:\n").strip()
                doc = myCollection.find_one({"review_id": rev_id})
                if doc:
                    print(doc)
                else:
                    print("Document not found.")
                    
            elif sub_choice == "2":
                target_stars = input("\nAt least how many stars:\n").strip()
                query = {"stars": {"$gte": target_stars}}
                results = myCollection.find(query).limit(3)
                print()
                for doc in results:
                    print(doc)
                    
            elif sub_choice == "3":
                target_stars = input("\nLess than how many stars:\n").strip()
                query = {"stars": {"$lt": target_stars}}
                results = myCollection.find(query).limit(3)
                print()
                for doc in results:
                    print(doc)
                    
            elif sub_choice == "4":
                word = input("\nSearch the title for:\n").strip()
                query = {"review_title": {"$regex": f".*{word}.*", "$options": "i"}}
                results = myCollection.find(query).limit(3)
                print()
                for doc in results:
                    print(doc)
                    
            elif sub_choice == "5":
                word = input("\nSearch the review for:\n").strip()
                query = {"review_body": {"$regex": f".*{word}.*", "$options": "i"}}
                results = myCollection.find(query).limit(3)
                print()
                for doc in results:
                    print(doc)

        # --- 2. ADD A NEW DOCUMENT ---
        elif choice == "2":
            new_doc = {
                "review_id": input("Enter ReviewID:\n").strip(),
                "product_id": input("Enter ProductID:\n").strip(),
                "reviewer_id": input("Enter ReviewerID:\n").strip(),
                "stars": input("Enter Number of Stars:\n").strip(),
                "review_title": input("Enter Review Title:\n").strip(),
                "review_body": input("Enter Review Body Contents:\n").strip(),
                "language": input("Enter Language:\n").strip(),
                "product_category": input("Enter Product Category:\n").strip()
            }
            myCollection.insert_one(new_doc)
            print("New document inserted.\n")

        # --- 3. UPDATE FIELDS OF A DOCUMENT ---
        elif choice == "3":
            rev_id = input("What is the ReviewID you wish to update?\n").strip()
            field_name = input("Which field would you like to update?\n").strip()
            new_value = input("What would you like to change the value to?\n").strip()
            
            query = {"review_id": rev_id}
            update_op = {"$set": {field_name: new_value}}
            myCollection.update_one(query, update_op)
            
            print("New document has been updated to:")
            updated_doc = myCollection.find_one({"review_id": rev_id})
            print(updated_doc)
            print()

        # --- 4. DELETE A DOCUMENT ---
        elif choice == "4":
            rev_id = input("What is the ReviewID of the document you wish to delete?\n").strip()
            query = {"review_id": rev_id}
            myCollection.delete_one(query)
            print("Document deleted!\n")

        # --- 5. DELETE ALL DOCUMENTS FROM COLLECTION ---
        elif choice == "5":
            print("Removing all documents from the collection...")
            result = myCollection.delete_many({})
            print(f"Number of documents deleted: {result.deleted_count}\n")

        # --- 6. DELETE A COLLECTION ---
        elif choice == "6":
            myCollection.drop()
            print("Collection removed!\n")

        # --- 7. EXIT THE PROGRAM ---
        elif choice == "7":
            print("Program has ended!")
            break
        else:
            print("Invalid selection. Please choose 1-7.\n")

if __name__ == "__main__":
    main()
