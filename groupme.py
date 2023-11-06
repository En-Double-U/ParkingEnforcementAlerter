from groupy import Client
import time
import messager

token = "TQdPA8IsV2rxKY5RMgVPEkRRbeYHGPAJjAcqa59m"
client = Client.from_token(token)
sender_credentials = ("groupmetextbot@gmail.com", "hagycxjkhaczabdl")

people = {
    "Nick Wang": ['39'],
}

def main():

    groups = list(client.groups.list_all())

    for i in range(len(groups)):
        if groups[i].name == 'bottesting':
            bottesting_index = i
            bottesting_group = groups[i]
        if 'PACE' in groups[i].name:
            pace_index = i
            pace_group = groups[i]

    try:
        newest_message = ""
        while(True):
            messages = pace_group.messages.list()

            # if there's a newer message than the old newest: do something
            print("newest", newest_message)
            print("last message", messages[0].text)
            if newest_message != messages[0].text:
                newest_message = messages[0].text
                print(newest_message)

                for name, info in people.items():
                    lot = info[0]
                    if lot in newest_message:
                        print("sending message")
                        message = "Your lot: " + lot + " has been mentioned in the PACE spottings group chat with the message: \n\n" + newest_message
                        subject = "PACE Spotted Near You!"

                        messager.pushbullet_noti(subject, message)
                        time.sleep(5)

            time.sleep(10)
    except Exception as e:
        print("restarting with error: ", e)
        # restart()


def restart():
    main()


if __name__ == "__main__":
    main()