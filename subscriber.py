import tkinter as tk
import paho.mqtt.client as mqtt
import time

mqtt_broker = "m2m.eclipse.org"
topic = "tp/eng/iotp_lab/project_05"

my_mqtt = None

def onMessage(client, userdata, message):
    print(message.payload)
    #change lblTemp text

def init():
    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack()

    label_1 = tk.Label(root, text="Fish Farm Temperature")
    lblTemp = tk.Label(root, text="")
    label_1.pack()
    lblTemp.pack()

    my_mqtt = mqtt.Client()
    my_mqtt.on_message = onMessage

    my_mqtt.connect(mqtt_broker, port=1883)
    my_mqtt.subscribe(topic, qos=0)
    my_mqtt.loop_start()

    root.mainloop()

def main():
    init()
    while True:
        time.sleep(2)

if __name__ == '__main__':
    main()
