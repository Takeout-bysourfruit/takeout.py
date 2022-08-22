from takeout import TakeoutClient
TakeoutClient.login('token')

emailTemplate = {
    'to': 'test@example.com',
    'from': 'Takeout.py', # as of July 2022, this will be (e.g) 'Takeout.py via Takeout' for free users
    'subject': 'I just sent an email using Takeout!',
    'text': 'My first email!',
}

TakeoutClient.send(**emailTemplate)