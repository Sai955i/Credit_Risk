import pandas as pd
import ace_tools as tools
import speech_recognition as sr  # Importing speech recognition library

# Creating a structured table of questions with placeholder for answers and examples
questions = [
    "What is MongoDB and how is it different from relational databases?",
    "What is a document in MongoDB?",
    "What is a collection in MongoDB?",
    "What is schema-less in MongoDB?",
    "What are the advantages of using MongoDB for data modeling?",
    "How does MongoDB store data internally?",
    "What is the BSON format?",
    "Can you explain embedded vs referenced documents in MongoDB?",
    "When would you choose embedding vs referencing in a MongoDB schema?",
    "What are the data types supported by MongoDB?",
    "What is a primary key in MongoDB?",
    "How does MongoDB handle relationships?",
    "Can we use joins in MongoDB like in SQL?",
    "Explain normalization and denormalization in the context of MongoDB.",
    "What are the best practices for designing a schema in MongoDB?",
    "How would you model a one-to-many relationship in MongoDB?",
    "How would you model a many-to-many relationship in MongoDB?",
    "Explain polymorphic schemas and when to use them.",
    "What is a capped collection and when would you use it?",
    "How does MongoDB handle indexing and how does that impact schema design?",
    "What are the different types of indexes in MongoDB relevant to data modeling?",
    "How would you model hierarchical data (like category trees) in MongoDB?",
    "What is the bucket pattern in MongoDB schema design?",
    "What is the outlier pattern and how is it useful in MongoDB?",
    "Can you explain the computed pattern in schema design?",
    "What is the subset pattern and when should it be applied?",
    "Explain how write/read patterns influence your MongoDB schema design.",
    "What are the tradeoffs between using an embedded document vs a referenced document?",
    "How would you model time-series data in MongoDB?",
    "What are schema anti-patterns in MongoDB, and how do you avoid them?",
    "Explain how MongoDB’s aggregation pipeline can support or hinder a particular data model.",
    "How does MongoDB's sharding affect schema design?",
    "What is the working set in MongoDB and how does it relate to schema design?",
    "How do you ensure data consistency in a NoSQL schema?",
    "How would you model a multi-tenant application in MongoDB?",
    "How would you structure user-role-permission management in MongoDB?",
    "Explain the impact of schema design on horizontal scaling in MongoDB.",
    "How can you migrate or refactor an existing schema in MongoDB safely?",
    "How would you handle schema validation in MongoDB?",
    "What are the implications of schema versioning in MongoDB?",
    "How does MongoDB's flexible schema support Agile development or microservices?",
    "Have you used MongoDB Atlas, and how does it impact your schema design approach?",
    "How would you optimize read-heavy vs write-heavy workloads in schema design?",
    "Can you explain change streams and how they relate to modeling for event-driven systems?",
]

df_questions = pd.DataFrame(questions, columns=["MongoDB Data Modeling Interview Questions"])

# Adding links to answers for each question
answer_links = [
    "https://www.mongodb.com/docs/manual/introduction/",
    "https://www.mongodb.com/docs/manual/core/document/",
    "https://www.mongodb.com/docs/manual/core/databases-and-collections/",
    "https://www.mongodb.com/docs/manual/core/schema-design/",
    "https://www.mongodb.com/docs/manual/core/data-modeling-introduction/",
    "https://www.mongodb.com/docs/manual/faq/storage/",
    "https://www.mongodb.com/docs/manual/reference/bson-types/",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#embedded-data-models",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#referenced-data-models",
    "https://www.mongodb.com/docs/manual/reference/bson-types/",
    "https://www.mongodb.com/docs/manual/core/document/#primary-key",
    "https://www.mongodb.com/docs/manual/core/data-model-design/",
    "https://www.mongodb.com/docs/manual/reference/sql-comparison/#joins",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#normalization-vs-denormalization",
    "https://www.mongodb.com/docs/manual/core/schema-design/",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#one-to-many",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#many-to-many",
    "https://www.mongodb.com/docs/manual/core/schema-design/#polymorphic-schemas",
    "https://www.mongodb.com/docs/manual/core/capped-collections/",
    "https://www.mongodb.com/docs/manual/indexes/",
    "https://www.mongodb.com/docs/manual/indexes/#index-types",
    "https://www.mongodb.com/docs/manual/tutorial/model-tree-structures/",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#bucket-pattern",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#outlier-pattern",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#computed-pattern",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#subset-pattern",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#read-write-patterns",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#embedded-vs-referenced",
    "https://www.mongodb.com/docs/manual/tutorial/model-time-series-data/",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#anti-patterns",
    "https://www.mongodb.com/docs/manual/aggregation/",
    "https://www.mongodb.com/docs/manual/core/sharding-introduction/",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#working-set",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#data-consistency",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#multi-tenancy",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#user-role-permission",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#horizontal-scaling",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#schema-migration",
    "https://www.mongodb.com/docs/manual/core/schema-validation/",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#schema-versioning",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#agile-development",
    "https://www.mongodb.com/docs/atlas/",
    "https://www.mongodb.com/docs/manual/core/data-model-design/#read-heavy-vs-write-heavy",
    "https://www.mongodb.com/docs/manual/changeStreams/",
]

df_questions["Answer Links"] = answer_links

tools.display_dataframe_to_user(name="MongoDB Interview Questions with Links", dataframe=df_questions)

# Function to capture voice input
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your question...")
        try:
            audio = recognizer.listen(source)
            voice_input = recognizer.recognize_google(audio)
            print(f"Recognized: {voice_input}")
            return voice_input
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

# Function to display the answer for a selected question
def get_answer_for_question():
    print("Do you want to select a question manually or use voice input?")
    choice = input("Type 'manual' for manual selection or 'voice' for voice input: ").strip().lower()

    if choice == "manual":
        print("Here are the available questions:")
        for i, question in enumerate(questions, start=1):
            print(f"{i}. {question}")
        try:
            question_number = int(input("Enter the question number: "))
            if 1 <= question_number <= len(questions):
                answer_link = df_questions.iloc[question_number - 1]['Answer Links']
                tools.display_text_to_user(f"Answer Link: {answer_link}")
            else:
                print("Invalid question number.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "voice":
        voice_input = get_voice_input()
        if voice_input:
            matched_question = None
            for question in questions:
                if voice_input.lower() in question.lower():
                    matched_question = question
                    break
            if matched_question:
                answer_link = df_questions[df_questions["MongoDB Data Modeling Interview Questions"] == matched_question]["Answer Links"].values[0]
                tools.display_text_to_user(f"Matched Question: {matched_question}\nAnswer Link: {answer_link}")
            else:
                print("No matching question found.")
    else:
        print("Invalid choice. Please type 'manual' or 'voice'.")

# Call the function to allow user interaction
get_answer_for_question()
