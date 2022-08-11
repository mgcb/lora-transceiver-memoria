import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

myMQTTClient = AWSIoTMQTTClient("brideMQTT") #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint("a2cv8tw2wojjxr-ats.iot.us-east-2.amazonaws.com", 8883)

myMQTTClient.configureCredentials("/home/pi/aws-iot/root-ca.pem", "/home/pi/aws-iot/private.pem.key", "/home/pi/aws-iot/certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()

def loop():
    while True:
        message = "Hello from the local gateway"
        print("Sending Message: ", message)


        myMQTTClient.publish(
            topic="RealTimeDataTrasfer/Message",
            QoS=1,
            payload='{"Message":"'+message+'"}')
        
        break

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        pass