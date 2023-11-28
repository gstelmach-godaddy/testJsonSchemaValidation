import json
import fastjsonschema


if __name__ == '__main__':


    with open("transaction_v2_schema.json", "r") as read_file:
        schema = json.load(read_file)
    with open("transaction_v2_messsage.json", "r") as read_message_file:
        message = json.load(read_message_file)

    validator = fastjsonschema.compile(schema)
    validator(message)


