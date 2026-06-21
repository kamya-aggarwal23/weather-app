def clean_message(text):
    text.strip().lower()
    return text
def clean_all(messages):
    for i in messages:
        clean_message(i)
        return i
messages = [
    "  Hello, I need help!  ",
    "MY ORDER IS DELAYED.  ",
    "  please refund me. ",
    "URGENT: account locked  "
]

user_profiles = {
    "U001": {"name": "Arjun",  "messages_sent": 0, "segment": "standard"},
    "U002": {"name": "Priya",  "messages_sent": 0, "segment": "standard"},
    "U003": {"name": "Ravi",   "messages_sent": 0, "segment": "standard"}
}
clean_all(messages)