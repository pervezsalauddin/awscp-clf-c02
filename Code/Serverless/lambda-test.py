import json

def lambda_handler(event, context):
    # TODO implement
    print('This is my AWS Lambda functon')
    if event['planet'] == 'Earth':
        return 'Moon'
    if event['planet'] == 'Jupiter':
        return 'Europa'
    elif event['planet'] == 'Sun':
        return 'This is not a Planet'
    else:
        return 'I do not recognize your argument!'