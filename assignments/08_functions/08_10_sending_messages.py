
# 8-10 Sending Messages: Print and move messages to a sent list.
def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(f"Sending: {message}")
        sent_messages.append(message)


messages = ["Hey!", "How are you?", "See you later!"]
sent_messages = []

show_messages(messages)
send_messages(messages, sent_messages)

print("Messages left:", messages)
print("Sent messages:", sent_messages)
