#!/bin/python
import boto3
import sys
import time
new_account_name=raw_input('Please enter account name to create: ')
new_account_email=raw_input('Please enter account email: ')

def list_accounts():
    aws_accounts=list()
    client = boto3.client('organizations')
    response = client.list_accounts(MaxResults=2)
    #print(response['NextToken'])
    while True:
      for existing_accounts in response['Accounts']:
        account_name=existing_accounts['Name']
        account_email=existing_accounts['Email']
        aws_accounts.append(account_name)
        aws_accounts.append(account_email)
      if 'NextToken' in response:
        response = client.list_accounts(NextToken=response['NextToken'],MaxResults=2)
      else:
        break
    return aws_accounts

def check_present():
    current_accounts = list_accounts()
    for i in (current_accounts):
        if new_account_name==(i):
           print('Account name exists. Use different name')
         #  break
           sys.exit(1)
        elif new_account_email==(i):
           print('Account email already used. Use different email')
           break
           sys.exit(1)

def create_account_in_org():
    client = boto3.client('organizations')
    response = client.create_account(
        Email=new_account_email,
        AccountName=new_account_name,
    )
    time.sleep(10)
    status=response['CreateAccountStatus']['State']
    requestID=response['CreateAccountStatus']['Id']
    print(response)
    if status!='SUCCEEDED':
        time.sleep(10)
        response=client.describe_create_account_status(CreateAccountRequestId=requestID)
	while response['CreateAccountStatus']['State']=='IN_PROGRESS':
            time.sleep(2)
 	    response=client.describe_create_account_status(CreateAccountRequestId=requestID)
	    print(response)
    response=client.describe_create_account_status(CreateAccountRequestId=requestID) 
    final_status=response['CreateAccountStatus']['State']
    if final_status=='SUCCEEDED':
        AccountID=response['CreateAccountStatus']['AccountId']
        print('Account {} Created'.format(AccountID))
    elif final_status=='FAILED':
        fail_reason=response['CreateAccountStatus']['FailureReason']
        print('Account creation failed due to {}'.format(fail_reason))
    

def main():
    check_present()
    create_account_in_org()

if __name__ == '__main__':
  main()
