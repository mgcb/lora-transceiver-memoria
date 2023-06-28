# lora_transceiver
Transmisor LoRa para comunicación peer-to-peer con Rapsberry PI con Dragino LoRa GPS hat

## Introducción
El software en este repositorio proviene de la base del código disponible en:

https://github.com/dragino/rpi-lora-tranceiver/tree/master/dragino_lora_app

Depende del Dragino HAT GPS para Raspberry PI

https://wiki.dragino.com/index.php?title=Lora/GPS_HAT

## Instalación

Clonar este repositorio con git clone

git clone https://github.com/mgcb/lora-transceiver-memoria.git

Verificar que  wiringPI este instalado. En caso de que no esté instalado: apt-get install wiringpi

```
cd lora-transceiver-memoria
make clean; make; make install
```

Para comprobar que servicio creado está corriendo correctamente

```
root@lorabase:/opt/lora_transceiver# systemctl status lora**●** lora.service - Starts the lora transceiver.

   Loaded: loaded (/lib/systemd/system/lora.service; enabled; vendor preset: enabled)

   Active: **active (running)** since Sat 2019-02-02 21:13:42 UTC; 7min ago

 Main PID: 23918 (lora_transceive)

   CGroup: /system.slice/lora.service

​           `└─23918 /usr/bin/lora_transceiver`

Feb 02 21:13:42 lorabase systemd[1]: Started Starts the lora transceiver..

```