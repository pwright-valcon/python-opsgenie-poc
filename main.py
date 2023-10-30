import os
import opsgenie_sdk

API_KEY = os.environ['OPSGENIE_API_KEY']


def create_alert():
    conf = opsgenie_sdk.configuration.Configuration()
    conf.api_key['Authorization'] = API_KEY
    conf.host = 'https://api.eu.opsgenie.com'

    api_client = opsgenie_sdk.api_client.ApiClient(configuration=conf)
    alert_api = opsgenie_sdk.AlertApi(api_client=api_client)

    body = opsgenie_sdk.CreateAlertPayload(
        message='Test alert',
        description='Test alert',
        priority='P3'
    )
    create_response = alert_api.create_alert(create_alert_payload=body)
    print(create_response)

    return create_response


if __name__ == '__main__':
    create_alert()
