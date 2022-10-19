# read the csv file
import pandas as pd
from datetime import datetime
from twilio.rest import Client

account_sid = "AC8bc883b7279ec260470f402a216a336f"
auth_token = "32e3f37f4d272a156745341b942902d1"


def retrieve_csv_file():
    print("reading Csv file")
    data = pd.read_csv("loan-list.csv")
    print("csv file read")
    return data


def perform_computation(datas):
    print("Performing Computation")
    my_list = []
    for (index, row) in datas.iterrows():
        given_date = datetime.strptime(row["given_date"], "%Y/%m/%d")
        return_date = datetime.strptime(row["return_date"], "%Y/%m/%d")
        # date_differ = return_date - datetime.today()
        date_differ = return_date - given_date
        new_dict = {}

        if date_differ.days < 6:
            new_dict["name"] = row["name"]
            new_dict["amount"] = row["amount"]
            new_dict["phone_number"] = row["phone_number"]
            new_dict["days_left"] = date_differ.days
            my_list.append(new_dict)
    print("returning the user ")
    return my_list


def send_message(peoples_to_pay):
    print("In The message function")
    for people in peoples_to_pay:
        print("in the loop")
        client = Client(account_sid,auth_token)
        message = client.messages.create(
            body=f"Hello Dear we Have lend You {people['amount']} Birr time to return it immediately",
            from_="+12058839599",
            to=f"+251{people['phone_number']}"
        )
        print(message.status)


data_from_csv = retrieve_csv_file()
dict_from_comp = perform_computation(data_from_csv)
send_message(dict_from_comp)

