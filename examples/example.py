from takeout import TakeoutClient
TakeoutClient.login('token')

file = TakeoutClient.getHTMLFileContents('test.html')
emailTemplate = {
    'to': 'test@example.com',
    'from': 'Takeout.py', # as of July 2022, this will be (e.g) 'Takeout.js via Takeout' for free users
    'subject': 'I just sent an email using Takeout!',
    'html': file,
}

TakeoutClient.send(**emailTemplate)