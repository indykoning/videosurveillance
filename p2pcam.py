import Camera as Cam
import base64

REQUIREMENTS = ['opencv-python=4.0.0.21']
DOMAIN = 'p2pcam'
hassio = None
name = "p2p"


def setup(hass, config):
    hassio = hass
    camera = Cam.P2PCam("192.168.178.5", "192.168.178.157")
    camera.onJpegReceived = saveFile
    camera.start()


def saveFile(cam, jpeg):
    print("data:image/jpeg;base64,"+base64.b64encode(jpeg))
    hassio.states.set('camera.' + name + '.entity_picture', "data:image/jpeg;base64,"+base64.b64encode(jpeg))
