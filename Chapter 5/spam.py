x = input("Enter your message. ")
y = ["buy now", "subscribe", "click here", "limited time offer", "free gift", "urgent", "act now"]
if x.lower() in y:
    print("This message is spam.")
else:
    print("This message is not spam.")

