import boto3, json, logging
from datetime import datetime

# Define logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SUBJECT = 'Py-SES PING'  # Subject line for email
BODY = 'Scheduled task:'  # Body of email

def send_email(ses: boto3.Session, sender: str, recipient: str, subject: str, body: str) -> None:
    """
    Function to send an email using AWS SES service.

    Args:
    ses (boto3 SES Client): The SES client object.
    sender (str): The sender's email address. Must be verified in AWS SES.
    recipient (str): The recipient's email address. Must be verified in AWS SES.
    subject (str): The subject line of the email.
    body (str): The body of the email.
    """
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")  # Get current time
    body = f'{body} {now}'  # Add current time to body of email
    res = ses.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [
                recipient
            ]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }
    )
    logger.info(f"Email sent! Status: {res['ResponseMetadata']['HTTPStatusCode']}, From: {sender}, To: {recipient}")


def sendEmails(credentials: list) -> None:
    """
    Function to send emails for each sender in the credentials list.

    Args:
    credentials (list): List of dictionaries where each dictionary contains sender details including AWS SES keys and email addresses.
    """
    for sender in credentials:
        try:
            required_keys = ['aws_access_key_id', 'aws_secret_access_key', 'email', 'ping_email', 'region']
            if not all(key in sender for key in required_keys):
                logger.warning(f"Missing credentials for {sender}")
                continue

            ses = boto3.client(
                'ses',
                aws_access_key_id=sender['aws_access_key_id'],
                aws_secret_access_key=sender['aws_secret_access_key'],
                region_name=sender['region']
            )
            send_email(ses, sender['email'], sender['ping_email'], SUBJECT, BODY)

        except Exception as e:
            logger.error(f"Error: {e} for sender {sender}")

def load_credentials(file_path):
    """
    Function to load email credentials from a JSON file.

    Args:
    file_path (str): The path to the JSON file containing email credentials.

    Returns:
    list: A list of dictionaries where each dictionary contains sender details including AWS SES keys and email addresses.
    """
    try:
        with open(file_path) as f:
            data = json.load(f)
        if not data:
            logger.error("Invalid json file")
            return None

        credentials = data.get('emails_credentials')  # List of emails to send from
        if not credentials:
            logger.error("No credentials found")
            return None

        return credentials
    except Exception as e:
        logger.error(f"Error: {e}")
        return None

if __name__ == '__main__':
    credentials = load_credentials('api_emails.json')
    if credentials:
        sendEmails(credentials)
