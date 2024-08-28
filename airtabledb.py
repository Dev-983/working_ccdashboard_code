import requests
import json
import time

def getDataFromPrograms():
  url = "https://api.airtable.com/v0/appWEthfvqsYcS0JG/Programs"
  headers = {
    'Authorization': 'Bearer patO3q6noIfzawBRE.2da1385e6c37631c54975c870ebaf68c07329c7014abe3e0f9e08ca7e68ba585'
   }
  response = requests.request("GET", url, headers=headers)
  data = json.loads(response.text)
# Access the list of records
  records = data['records']
  projects = {}
  for record in records:
    record_id = record['id']
    created_time = record['createdTime']
    fields = record['fields']

    
    end_date = fields.get('End date')
    start_date = fields.get('Start date')
    budget = fields.get('Project Budget')
    program_name = fields.get('Program name')
    description = fields.get('Description')
    status = fields.get('Status')

    projects[record_id]={'name':program_name,'status':status,'start_date':start_date,'end_date':end_date,'ProjectBudget':budget}
  
  return  projects

def create_record_Program(name,totalcost,d1,d2):

  url = "https://api.airtable.com/v0/appWEthfvqsYcS0JG/Programs"
  data2 = {
    "fields": {
        "Program name": name,
        "Description": "This is test work Project.",
        "Start date": d1,
        "End date": d2,
        "Status": "In Progress",
        "Project Budget": int(totalcost)
    }
  }
  print(data2)
  # Convert the dictionary to a JSON string
  payload2 = json.dumps(data2)  
  headers2 = {
    'Authorization': 'Bearer patO3q6noIfzawBRE.2da1385e6c37631c54975c870ebaf68c07329c7014abe3e0f9e08ca7e68ba585',
    'Content-Type': 'application/json'
  }
  
  try:
    # Make the POST request
    response = requests.post(url, headers=headers2, data=payload2)
    # Check if the request was successful
    response.raise_for_status()
    ##print('Response Status Code:', response.status_code)
    ##print('Response JSON:', response.json())
    return 'success'

  except requests.exceptions.HTTPError as http_err:
    #print(f'HTTP error occurred: {http_err}')
    return "error"
  except requests.exceptions.ConnectionError as conn_err:
    #print(f'Connection error occurred: {conn_err}')
    return "error"
  except requests.exceptions.Timeout as timeout_err:
    #print(f'Timeout error occurred: {timeout_err}')
    return "error"
  except requests.exceptions.RequestException as req_err:
    #print(f'Request error occurred: {req_err}')
    return "error"
  except Exception as err:
    #print(f'An error occurred: {err}')
    return "error"
  
def add_list(arr,ids):
  for entry in arr:
    title = entry['title']
    start_time = entry['startTime']
    description = entry['description']

    url = "https://api.airtable.com/v0/appWEthfvqsYcS0JG/studytimeline"
    dataset3 = { "fields": {
        "Title": title,
        "Description": description,
        "Date":start_time,
        "programid": ids,
        "status":'todo'
      }}
    payload3 = json.dumps(dataset3)

    headers3 = {
      'Authorization': 'Bearer patO3q6noIfzawBRE.2da1385e6c37631c54975c870ebaf68c07329c7014abe3e0f9e08ca7e68ba585',
      'Content-Type': 'application/json',   
    }
    try:

      response = requests.request("POST", url, headers=headers3, data=payload3)
      response.raise_for_status()
      return 'success'
    except requests.exceptions.HTTPError as http_err:
      #print(f'HTTP error occurred: {http_err}')
      return "error"
    except requests.exceptions.ConnectionError as conn_err:
      #print(f'Connection error occurred: {conn_err}')
      return "error"
    except requests.exceptions.Timeout as timeout_err:
      #print(f'Timeout error occurred: {timeout_err}')
      return "error"
    except requests.exceptions.RequestException as req_err:
      #print(f'Request error occurred: {req_err}')
      return "error"
    except Exception as err:
      #print(f'An error occurred: {err}')
      return "error"

    time.sleep(6)
  return  'Success'

def getList():
  url = "https://api.airtable.com/v0/appWEthfvqsYcS0JG/studytimeline"
  headers = {
    'Authorization': 'Bearer patO3q6noIfzawBRE.2da1385e6c37631c54975c870ebaf68c07329c7014abe3e0f9e08ca7e68ba585'
   }
  response = requests.request("GET", url, headers=headers)
  data = json.loads(response.text)
# Access the list of records
  records = data['records']
  projects = {}
  for record in records:
    record_id = record['id']
    created_time = record['createdTime']
    fields = record['fields']
    
    title = fields.get('Title')
    date = fields.get('Date')
    ids = fields.get('programid')
    description = fields.get('Description')
    status = fields.get('Status')

    projects[ids]={'title':title,'status':status,'date':date,'description':description}
  
  return  projects
