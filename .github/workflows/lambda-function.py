import json
import random

def lambda_handler(event, context):
    # Generate a random number between 1 and 100
    random_num = random.randint(1, 100)

    # Create a JSON response with the random number
    response = {
        'statusCode': 200,
        'body': json.dumps({'random_number': random_num})
    }

    return response
