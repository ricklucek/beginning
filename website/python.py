from google.cloud import storage

import cgi

form = cgi.FieldStorage()

nome = form.getvalue(key = "usuario_nome")
email = form.getvalue(key = "usuario_email")
msg = form.getvalue(key = "usuario_msg")

print nome, email, msg

client = storage.Client()
bucket = client.get_bucket('henrique2022.appspot.com')

bucket.blob('nome :{0}, email:{1}, mensagem:{2}'.format(nome, email, msg)).upload_from_string(nome, 'text')

print "uploaded to {}.".format(bucket)