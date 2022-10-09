import requests

authenticated = None
auth_token = None

send_url = "https://takeout.bysourfruit.com/api/email/send"
auth_url = "https://takeout.bysourfruit.com/api/auth/verify"

class TakeoutClient:
    @staticmethod
    def login(token):
        global authenticated
        global auth_token

        if token is None:
            exit("Takeout Login Error! A token wasn't provided")

        loginAttempt = requests.post(auth_url, json = {"token": token}, headers= {"Content-Type": "application/json"}, verify=True)
        loginJSON = loginAttempt.json()

        if loginAttempt.status_code > 200:
            authenticated = False
            exit(f'Takeout Login Error! {loginJSON["message"]}')

        if loginAttempt.status_code == 200:
            authenticated = True
            auth_token = token
            print("Authenticated successfully.")

        if loginAttempt.status_code == 500:
            exit("Takeout's currently having some issues server-side. These may be temporary issues caused by maintenance, or they may be caused by your input/Takeout.py.")


    @staticmethod
    def send(**kwargs):
        if not authenticated:
            exit("Takeout Send Error! You're not logged in! Run TakeoutClient.login(token)")

        sender = kwargs.get("from").strip()
        receiver = kwargs.get("to").strip()
        subject = kwargs.get("subject").strip()
        bodyText = kwargs.get("text", "")
        bodyHTML = kwargs.get("html", "")
        # Added in 1.2.2
        cc = kwargs.get("cc", "")
        replyTo = kwargs.get("replyTo", "")

        if not sender or not receiver or not subject:
            exit("Takeout Send Error! One of the required fields to send an email was not fulfilled. Check if your receiver, sender, and subject are defined.")

        else:
            sendData = {
                # Removed token
                "sender": sender,
                "receiver": receiver,
                "subject": subject,
                # No bodies, yet !
                # No CC or reply-to !
            }

            if bodyText:
                sendData.update({"bodyText": bodyText})

            if bodyHTML:
                sendData.update({"bodyHTML": bodyHTML})

            if bodyHTML and bodyText:
                sendData.update({"bodyHTML": bodyHTML})

            if cc:
                sendData.update({"cc": cc})

            if replyTo:
                sendData.update({"replyTo": replyTo})

            # if not bodyText and not bodyHTML:
                # print("You've supplied no bodies, but Takeout will send it along anyways...")

            sendAttempt = requests.post(send_url, json=sendData, headers={"Content-Type": "application/json", "Authorization": f'Token {auth_token}'}, verify=True)
            sendJSON = sendAttempt.json()

            if sendAttempt.status_code == 200:
                print("Sent email successfully.")

            if sendAttempt.status_code == 500:
                exit("Takeout's currently having some issues server-side. These may be temporary issues caused by maintenance, or they may be caused by your input/Takeout.py.")

            if sendAttempt.status_code > 200:
                exit(f'Takeout Send Error! {sendJSON["message-id"]}')


    @staticmethod
    def getLocalTemplate(path):
        try:
            file = open(path, mode='r')
            all_of_it = file.read()
            file.close()
            return all_of_it
        except IOError:
            exit("Takeout File Error! File doesn't seem to exist")


    @staticmethod
    def getCloudTemplate(name):
        templateReq = requests.get(f'https://cdn-takeout.bysourfruit.com/cloud/read?name={name}&token={auth_token}', verify=True)

        if templateReq.status_code == 400:
            exit("Takeout didn't get a token, or you're not a Takeout+ subscriber")

        return templateReq.text
