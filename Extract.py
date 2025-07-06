from faker import Faker
import csv
import random
import string

# Initialize Faker
fake = Faker()

# Helper to generate a secure password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate one employee record
def generate_employee_data(employee_id):
    return {
        "EmployeeID": employee_id,
        "FullName": fake.name(),
        "Email": fake.email(),
        "Password": generate_password(),  # Secure password
        "PhoneNumber": fake.phone_number(),
        "Address": fake.address().replace("\n", ", "),
        "DateOfBirth": fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat(),
        "SSN": fake.ssn(),
        "JobTitle": fake.job(),
        "Department": random.choice(["HR", "Engineering", "Marketing", "Sales", "Finance", "Support"]),
        "Salary": round(random.uniform(50000, 150000), 2),  # Salary in USD
        "JoinDate": fake.date_between(start_date='-10y', end_date='today').isoformat(),
        "Nationality": fake.country(),
    }

# Function to generate and save to CSV
def generate_employee_csv(filename, count=100):
    fieldnames = [
        "EmployeeID", "FullName", "Email", "Password", "PhoneNumber", "Address",
        "DateOfBirth", "SSN", "JobTitle", "Department", "Salary",
        "JoinDate", "Nationality"
    ]
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, count + 1):
            writer.writerow(generate_employee_data(i))

    print(f"{count} dummy employee records saved to '{filename}'.")

# Run the script
if __name__ == "__main__":
    generate_employee_csv("dummy_employees.csv", count=100)

from google.cloud import storage

def upload_to_gcs(bucket_name, source_file_path, destination_blob_name):
    client = storage.Client(project="cool-phalanx-464921-n7")  # <--- pass your project here
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path)
    print(f" Uploaded {source_file_path} to gs://{bucket_name}/{destination_blob_name}")

if __name__ == "__main__":
    upload_to_gcs(
        bucket_name="sk-employeee-data",  # double-check spelling of your bucket name
        source_file_path="dummy_employees.csv",
        destination_blob_name="employees/dummy_employees.csv"
    )


