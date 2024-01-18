
import fastjsonschema

sub_schemas = { "urn:shared:definitions.randomNumber": {"type": "integer"},
                "urn:shared:definitions.randomObject": {"$schema": "http://json-schema.org/draft-07/schema#", "type": "object", "properties": {"randomName": {"type": "string"}}, "required": ["randomName"]},
              }
def customer_ref_handler(ref: str):
    return sub_schemas[ref]

schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"$ref": "#/definitions/Age"},
            "phones": {
                "type": "array",
                "items": {"type": "string"}
            },
            "aNumber": {"$ref": "urn:shared:definitions.randomNumber"},
            "anObject": {"$ref": "urn:shared:definitions.randomObject"}
        },
        "required": ["name", "age", "aNumber"],
        "definitions": {
            "Age": {"type": "integer"}
        }
    }

message = {
        "name": "John Doe",
        "age": 43,
        "phones": [
            "+44 1234567",
            "+44 2345678"
        ],
        "aNumber": 2,
        "anObject": {"randomName": "John Doe"}

    }

if __name__ == '__main__':

    validator = fastjsonschema.compile(schema, handlers={'urn': customer_ref_handler})

    validator(message)





