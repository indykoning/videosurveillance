import logging

import voluptuous as vol

from homeassistant.const import CONF_NAME
from homeassistant.components.camera import Camera, PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = 'p2pcam'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})


async def async_setup_platform(hass, config, async_add_entities,
                               discovery_info=None):
    async_add_entities([P2PCam(hass, config)])


class P2PCam(Camera):
    def __init__(self, hass, config):
        import Camera as Cam

        super().__init__()

        self._name = config.get(CONF_NAME)

        self.camera = Cam.P2PCam("192.168.178.5", "192.168.178.9")

    async def async_camera_image(self):
        return self.camera.retrieveImage()

    @property
    def name(self):
        """Return the name of this camera."""
        return self._name
