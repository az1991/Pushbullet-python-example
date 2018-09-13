from pushbullet import Pushbullet

# PushBullet API Key
pb = Pushbullet("PUSHBULLET API KEY")

# PushBullet target device
target_device = pb.get_device('TARGET DEVICE ID')


def push_message(target_device,message):
    push_title = "Mssage title"
    push = target_device.push_note(push_title, message)


message="this is an example"
push_message(target_device,message)
