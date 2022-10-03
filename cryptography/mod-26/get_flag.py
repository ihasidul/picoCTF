import codecs

f = open("given_text", "r")
secret_key = f.read()
print(codecs.decode(secret_key,"rot_13"))