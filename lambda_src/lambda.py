import os
import time
from multiprocessing.connection import Client

print('[Lambda] Initializing lambda.')

def handler(event, context):
    print('[Lambda] Connecting to socket.')
    
    address = ('localhost', int(os.environ['SOCKET_PORT']))
    conn = None
    
    while conn == None:
        try:
            conn = Client(address)
        except:
            print('[Lambda] Socket not available')
            time.sleep(1)
    
    print('[Lambda] Sending messages to socket.')
    conn.send(f'Executing the lambda with the following payload: {event}')
    conn.send('message 1')
    conn.send('message 2')
    conn.send('message 3')
    conn.send('close')
    conn.close()

    print('[Lambda] Finishing execution!')

    return {
        "statusCode": 200,
        "body": "done!"
    } 