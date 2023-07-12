from bardapi import Bard


token = 'XQjUurKVRCZM2v-6zalGD9cEJ8tyU-_H-0tCPOWEsGLovLbzbAD6-7bL76cwxDIxp0W1Xw.'
bard = Bard(token=token)
response = bard.get_answer("What is machine learning?")['content']
print(response)