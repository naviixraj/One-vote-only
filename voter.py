import hashlib
import os

FILE_NAME = "votes.txt"

def hash_fingerprint(fingerprint):
    return hashlib.sha256(fingerprint.encode()).hexdigest()


def check_duplicate(college_id, fingerprint_hash):
    if not os.path.exists(FILE_NAME):
        return False

    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            parts = line.split(",")

            # Skip wrong formatted lines
            if len(parts) != 2:
                continue

            saved_id, saved_fp = parts

            if saved_id == college_id:
                return True

            if saved_fp == fingerprint_hash:
                return True

    return False


def store_data(college_id, fingerprint_hash):
    with open(FILE_NAME, "a") as file:
        file.write(college_id + "," + fingerprint_hash + "\n")


while True:
    print("\n---- Voting System ----")

    college_id = input("Enter College ID: ").strip()
    fingerprint = input("Enter Fingerprint (any unique text): ").strip().lower()

    fingerprint_hash = hash_fingerprint(fingerprint)

    if check_duplicate(college_id, fingerprint_hash):
        print("❌ Error: Already Voted!")
    else:
        store_data(college_id, fingerprint_hash)
        print("✅ Vote Successfully Recorded!")

    choice = input("Do you want to enter next voter? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Voting session ended.")

        break
