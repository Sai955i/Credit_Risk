import pandas as pd

def collect_data():
    # Create an empty list to store all the records
    records = []

    # Ask the user how many records they want to enter
    num_entries = int(input("How many entries do you want to enter? "))
    
    for _ in range(num_entries):
        # Prompt the user to input values
        user_input = input("Enter your name, age, salary, location, department, job title and experience (comma separated): ")
        # Split the input into variables
        name, age, salary, location, department, job_title, experience = user_input.split(",")
        
        # Add the data as a dictionary to the records list
        records.append({
            "Name": name.strip(),
            "Age": age.strip(),
            "Salary": salary.strip(),
            "Location": location.strip(),
            "Department": department.strip(),
            "Job Title": job_title.strip(),
            "Experience": experience.strip()
        })
    
    # Convert the records into a pandas DataFrame
    df = pd.DataFrame(records)
    
    # Save the DataFrame to an Excel file
    df.to_excel("employee_data1.xlsx", index=False)
    print("Data has been saved to employee1_data.xlsx")

if __name__ == "__main__":
    collect_data()
