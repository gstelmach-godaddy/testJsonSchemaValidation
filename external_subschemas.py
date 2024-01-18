
import fastjsonschema

sub_schemas = { "urn:shared:definitions.IntNumber": {"type": "integer"},
                "urn:shared:definitions.Address": {"$schema": "http://json-schema.org/draft-07/schema#", "type": "object", "properties": {"street1": {"type": "string"}, "city": {"type": "string"}}, "required": ["street1", "city"]},
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
            "aNumber": {"$ref": "urn:shared:definitions.IntNumber"},
            "address": {"$ref": "urn:shared:definitions.Address"}
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
        "address": {
            "street1": "123 Main St.",
            "city": "Katmandu"
        }

    }

if __name__ == '__main__':

    validator = fastjsonschema.compile(schema, handlers={'urn': customer_ref_handler})

    validator(message)





