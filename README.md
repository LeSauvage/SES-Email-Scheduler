# AWS SES Email Scheduler

AWS SES Email Scheduler is a Python-based script designed to send scheduled emails to [Healthchecks.io](https://healthchecks.io/), helping verify the working status of your emails. It uses AWS Simple Email Service (SES) to send the emails.

## Requirements
- Python 3.6+
- AWS Account with SES configured
- AWS IAM user with programmatic access and SES permissions
- Email address verified with AWS SES

## Installation

First, clone the repository to your local machine:

```
git clone git@github.com:LeSauvage/SES-Email-Scheduler.git
```

Navigate to the project directory:

```
cd aws-ses-email-scheduler
```

Install the required Python packages:

```
pip install -r requirements.txt
```

## Setup

Create a JSON file with the following format and fill in the necessary information for each email credential:

```json
{
	"emails_credentials": [
		{
			"email": "<Your_Email>",
			"aws_access_key_id": "<AWS_Access_Key>",
			"aws_secret_access_key": "<AWS_Secret_Key>",
			"region": "<AWS_Region>",
			"ping_email": "<Ping_Email>"
		},
		{
			"email": "<Your_Email>",
			"aws_access_key_id": "<AWS_Access_Key>",
			"aws_secret_access_key": "<AWS_Secret_Key>",
			"region": "<AWS_Region>",
			"ping_email": "<Ping_Email>"
		}
	]
}
```

- `email`: The verified email address from which you'll send emails.
- `aws_access_key_id`: The access key for your AWS IAM user.
- `aws_secret_access_key`: The secret key for your AWS IAM user.
- `region`: The AWS region in which you have verified your email address.
- `ping_email`: The email address where you want to send the email (typically the ping email for healthchecks.io).

## Usage

Simply run the Python script:

```
python mailSender.py
```

The script will load the email credentials from the JSON file and send an email to the specified recipient email address, for each credential in the list.

For scheduling the script, you can use various tools depending on your operating system. Some common choices include cron jobs on Unix-based systems and Task Scheduler on Windows.

## Support

If you encounter any problems or have any suggestions, please open an issue on this GitHub repository.

## License

This project is open source, under the terms of the [MIT License](https://opensource.org/licenses/MIT).
