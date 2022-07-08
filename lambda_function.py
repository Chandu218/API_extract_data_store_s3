import json
import boto3

def lambda_handler(event, context):
    try:
        destination_bucket = 'data-store-bkt'
        user_data = event
        if 'NumberofRecords' not in user_data.keys():
            print('Error. missing NumberofRecords')
            return json.dumps({'Status'.:'Error. Missing records'})
        file_name = str(user_data.get('NumberofRecords'))+'. json'
        s3_resource = boto3.resource('s3')
        object_handler = s3_resource.Object(destination_bucket, file_name)
        object_handler.put(Body=bytes(json.dumps(user_data),encoding='utf-8'))
        return json.dumps({'Status':'Success'})
     except Exception as e:
       print(e)
       return json.dumps({'Status':'Error in try block'})
