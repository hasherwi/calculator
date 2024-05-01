import json

def lambda_handler(event, context):
    # Extract operation and numbers from the event
    operation = event.get('operation', 'add')   # Default to 'add'
    number1 = float(event.get('number1', 0))    # Default to 0
    number2 = float(event.get('number2', 0))    # Default to 0

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
            'body': json.dumps('Invalid operation')
        }

    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }