<p align='center'><img src="https://i.ibb.co/s9kq3V0/takeout.png" height="150px"/></p>
<h1 align='center'>Takeout.py</h1>

<p align='center'>
    <img display="inline-block" src="https://img.shields.io/pypi/v/takeout.py?style=for-the-badge" /> <img display="inline-block" src="https://img.shields.io/badge/Made%20with-Python-green?style=for-the-badge" />
</p>
<p align='center'>Takeout.py is super easy to use. In under 10 lines of code, you can send an email to anyone, anywhere. Ah, the joys of the internet.</p>

## Installation 🏗
You can install Takeout.js using pip
```shell
$ pip install takeout.py
```

Then, import it like this:
```py
from takeout import TakeoutClient
```

## Setup 🛠
First, get your token from the [Takeout dashboard](https://takeout.bysourfruit.com/dashboard). You'll need it in a little bit.

Then, using that token you just got, use it here: 
```py
TakeoutClient.login('your token here')
```

As of right now, your code should look something like this:
```py
from takeout import TakeoutClient
TakeoutClient.login('your token here')
```

"But I want to actually send an email!" => we're getting there!  

## Sending your first email 📤

Define a 'template' similar to this: 
```py
emailTemplate = {
    'to': 'test@example.com',
    'from': 'Takeout.py', # This will be (e.g) 'Takeout.py via Takeout' for free users
    'subject': 'I just sent an email using Takeout!',
    'html': "<b>My first email!</b>",
}
```
or
```py
emailTemplate = {
    'to': 'test@example.com',
    'from': 'Takeout.py', # This will be (e.g) 'Takeout.py via Takeout' for free users
    'subject': 'I just sent an email using Takeout!',
    'text': 'My first email!',
}
```
and then... 
```py
TakeoutClient.send(**emailTemplate)
```
Note! Unlike Takeout.js, Takeout.py does not yet return an email ID.

See? It's super simple. Oh, and you can also import HTML directly from a file, using `getHTMLFileContents()`. 
This is demonstrated here: 
```py
file = TakeoutClient.getHTMLFileContents('test.html')
emailTemplate = {
    'to': 'test@example.com',
    'from': 'Takeout.py', # This will be (e.g) 'Takeout.py via Takeout' for free users
    'subject': 'I just sent an email using Takeout!',
    'html': file,
}

TakeoutClient.send(**emailTemplate)
```

## Additional fields
Takeout.py you to CC one person (a method to CC more is coming soon). Define this in your template. 
```py
emailTemplate = {
    'to': 'test@example.com',
    'from': 'Takeout.py', # This will be (e.g) 'Takeout.py via Takeout' for free users
    'subject': 'I just sent an email using Takeout!',
    'text': 'My first email!',
    'cc': 'test@notexample.com'
}
```

Furthermore, Takeout.py allows you to set a reply-to email. Define this in your template. 
```py
emailTemplate = {
    'to': 'test@example.com',
    'from': 'Takeout.py', # This will be (e.g) 'Takeout.py via Takeout' for free users
    'subject': 'I just sent an email using Takeout!',
    'text': 'My first email!',
    'replyTo': 'reply@tome.com'
}
```


## Errors
With the arrival of 1.2.0, came a new method to authenticate with Takeout's API. This removed your token from the request body and moved it to the Authorization header. If you're running an older version Takeout.py, Takeout will throw an error. Upgrade to a version >=1.2.0

## Roadmap 🚦
- Some sort of templating built in, allowing you a greater variety of options in a single package (with... well some dependencies). 
- Fixing SMTP email validation.
- Bug fixes.
- A lot more.

### See complete examples in [examples/](https://github.com/s0urfruit/takeout.py/tree/main/examples)