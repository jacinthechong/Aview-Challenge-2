import requests
from google.cloud import firestore

def lambda_handler(event, context):
  try:
    # Fetch data from the external API - random cat image and details
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    response.raise_for_status()
    response_json = response.json()

  # Connect to Firestore
    firestore_client = firestore.Client.from_service_account_json('./service_account.json')

  # Store the data in Firestore
    doc_ref = firestore_client.collection('cat-images').document(response_json[0]['id'])

    doc_ref.set(response_json[0])
    print("Entered into database:", response_json[0])
    return ("Entered into database:", response_json[0])

  except requests.exceptions.RequestException as e:
    print("Error occurred while fetching data:", str(e))
    return None

  except Exception as e:
    print("An error occurred:", str(e))
    return None