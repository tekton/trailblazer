import boto3

"""
	To keep all the AWS interactions together that aren't the base
	handlers, we'll shove it all in here just in case.
"""


def get_session():
	pass


def get_from_dynamo(table, pk_str, pk_val, aws_region="us-west-2", dynamo=None):
	if not dynamo:
		dynamo = boto3.client('dynamodb', region_name=aws_region)
	res = dynamo.get_item(
			TableName=table,
			Key={
				pk_str: {"S": pk_val}
			}
		)
	return res


def push_to_dynamo(table, data_dict, aws_region="us-west-2", dynamo=None):
	if not dynamo:
		dynamo = boto3.client('dynamodb', region_name=aws_region)
	try:
		res = dynamo.put_item(
				TableName=table,
				Item=data_dict,
				ConditionExpression="attribute_not_exists(s)"
			)
		return res
	except Exception as e:
		print(e)
		return e


if __name__ == "__main__":
	_table = "tbHash"
	_pk_str = "s"
	# create an entry to try to get later...

	data_dict = {
		_pk_str: {"S": "yxeo9Dmjh"},
		"u": {"S": "https://tks.pyroturtle.com"}
	}
	y = push_to_dynamo(table=_table, data_dict=data_dict)
	print(y)

	exit()
	x = get_from_dynamo(
			table=_table,
			pk_str=_pk_str,
			pk_val="qJURECmjhx"
		)
	if "Item" not in x:
		print("ERR: ", x)
	elif "u" not in x["Item"]:
		print("Unable to find URL")
	else:
		print(x["Item"]["u"]["S"])
