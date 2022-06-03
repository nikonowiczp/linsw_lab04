
openssl genrsa -out linsw.lab4.key 2048

openssl req -new -key linsw.lab4.key -out linsw.lab4.csr


openssl x509 -req -in linsw.lab4.csr -CA myCA.pem -CAkey myCA.key \
	-CAcreateserial -out linsw.lab4.crt -days 365 -sha256


