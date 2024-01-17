
import fastjsonschema
from jsonschema import validate

schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "age": {"$ref": "#/definitions/Age"},
        },
        "required": ["age"],
        "definitions": {
            "Age": {"$ref": "#/definitions/AgeDetail"},
            "AgeDetail": { "type": "integer" }
        }
    }

message = {
        "age": 43
    }

if __name__ == '__main__':

    try:
        print("\nTest fastjsonschema:")
        validator = fastjsonschema.compile(schema)
        validator(message)
        print("Valid!!")
    except Exception as e:
        print(f"Invalid!!: {e}")


    try:
        print("\nTest jsonschema:")
        validate(message, schema)
        print("Valid!!")
    except Exception as e:
        print(f"Invalid!!: {e}")