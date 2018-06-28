import boto3
def lambda_handler(event, context):
    aws_accounts=list()
    client = boto3.client('organizations')
    response = client.list_accounts(MaxResults=2)
#    print(response['NextToken'])
    while True:
      for existing_accounts in response['Accounts']:
        account_name=existing_accounts['Name']
        aws_accounts.append(account_name)
      if 'NextToken' in response:
        response = client.list_accounts(NextToken=response['NextToken'],MaxResults=2)
      else:
        break
    for i in (aws_accounts):
      print(i)
