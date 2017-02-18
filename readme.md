To log into ec2:
ssh -i "locus.pem" ubuntu@54.164.184.172


python webpy.py


test post requests:
curl -d "payload message" http://localhost:8080/hello/
or
http://requestmaker.com/    54.164.184.172:8080/hello/

