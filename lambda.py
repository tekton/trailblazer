import awslib
import boto3
import hasher
import json
import os

OFFSET = os.getenv("OFFSET", 0)
TABLE = os.getenv("TABLE", "tbHash")
URL_ROOT = os.getenv("URL_ROOT", "http://localhost:8000")
URL_STAGE = os.getenv("URL_STAGE", "dev")


def push_handler(event, context):

    rtn_dict = {
        "statusCode": 500,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"error": "system error"})
    }

    if event["httpMethod"] == "POST":
        body = json.loads(event["body"])
        if "u" not in body:
            rtn_dict["body"] = json.dumps({"error": "Unable to find item to shorten"})
            return rtn_dict
        else:
            u = body["u"]
    elif event["httpMethod"] == "GET":
        if "u" not in event["queryStringParameters"]:
            rtn_dict["body"] = json.dumps({"error": "Unable to find item to shorten"})
            return rtn_dict
        else:
            u = event["queryStringParameters"]["u"]
    else:
        rtn_dict["statusCode"] = 404
        rtn_dict["body"] = json.dumps({"error": "Unable to find a path of redemption"})
        return rtn_dict

    # The fun can begin!
    s = hasher.tbHash(offset=OFFSET)
    data_dict = {
        "s": {"S": s},
        "u": {"S": u}
    }
    res = awslib.push_to_dynamo(table=TABLE, data_dict=data_dict)
    print(res)

    # Did we get what we wanted?
    if "ResponseMetadata" in res:
        if res["ResponseMetadata"]["HTTPStatusCode"] == 200:
            rtn_dict["statusCode"] = 200
            rtn_dict["body"] = json.dumps({"short": s,
                                           "url": u,
                                           "uri": "{}/{}/".format(URL_ROOT, URL_STAGE, s)})
            return rtn_dict
        else:
            rtn_dict["body"] = json.dumps({"error": "unable to save"})
            return rtn_dict
    else:
        return rtn_dict


def get_handler(event, context):
    try:
        res = awslib.get_from_dynamo(
            table=TABLE,
            pk_str="s",
            pk_val=event["pathParameters"]["s"]
        )
        return {
            "statusCode": 302,
            "headers": {
                "Location": res["Item"]["u"]["S"]
            },
            "body": ""
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 404,
            "body": "unable to find"
        }


if __name__ == "__main__":
    ex_event = {
      "pathParameters": {
        "s": "yxeo9Dmjh"
      }
    }

    x = get_handler(ex_event, None)
    print(x)

    post_example = {
        "body": "{\"u\": \"http://pyroturtle.com\"}",
        "resource": "/print_request",
        "queryStringParameters": None,
        "multiValueHeaders": None,
        "multiValueQueryStringParameters": None,
        "pathParameters": None,
        "headers": None,
        "isBase64Encoded": False,
        "stageVariables": None,
        "path": "/print_request",
        "httpMethod": "POST"
    }

    x = push_handler(post_example, None)
    print(x)

    get_example = {
        "httpMethod": "GET",
        "queryStringParameters": {
            "u": "https://asdf.pyroturtle.com"
        },
        "multiValueHeaders": None,
        "multiValueQueryStringParameters": {
            "u": [
                "https://asdf.pyroturtle.com"
            ]
        }
    }

    x = push_handler(get_example, None)
    print(x)
