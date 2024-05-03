"""A simple calculator function for AWS Lambda."""

import json

def lambda_handler(event, context):
    """A simple calculator function for AWS Lambda."""

    # Log the entire event and context objects
    print("Event: ", json.dumps(event))
        # Convert the event dictionary to a JSON formatted string and print
    print("Context: ", context)
        # The context object is not serializable to JSON directly without custom handling

    # Check if query parameters exist
    query_params = event.get('queryStringParameters', {})

    # Extract operation and numbers from the event
    operation = query_params.get('operation', 'add')   # Default to 'add'
    number1 = float(query_params.get('number1', 0))    # Default to 0
    number2 = float(query_params.get('number2', 0))    # Default to 0

    # Perform operation
    if operation == 'add':
        result = number1 + number2
    elif operation == 'subtract':
        result = number1 - number2
    elif operation == 'multiply':
        result = number1 * number2
    elif operation == 'divide':
        result = number1 / number2 if number2 != 0 else 'undefined'
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid operation'),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    
    print("Result: ", result)

    return {
        'statusCode': 200,
        'body': json.dumps({'result': result}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
