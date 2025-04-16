from datetime import timedelta
from typing import Final

from homeassistant.const import Platform

NAME: Final = "Xiaomi Cloud Map Extractor"

DOMAIN: Final = "xiaomi_cloud_map_extractor"

PLATFORMS: list[Platform] = [
    Platform.CAMERA,
    Platform.IMAGE,
]

CONTENT_TYPE: Final = "image/png"
DEFAULT_UPDATE_INTERVAL: Final = timedelta(seconds=10)

CONF_USED_MAP_API: Final = "used_map_api"
CONF_SERVER: Final = "server"

CONF_IMAGE_CONFIG: Final = "image_config"
CONF_IMAGE_CONFIG_SCALE: Final = "scale"
CONF_IMAGE_CONFIG_ROTATE: Final = "rotate"
CONF_IMAGE_CONFIG_TRIM_LEFT: Final = "trim_left"
CONF_IMAGE_CONFIG_TRIM_RIGHT: Final = "trim_right"
CONF_IMAGE_CONFIG_TRIM_TOP: Final = "trim_top"
CONF_IMAGE_CONFIG_TRIM_BOTTOM: Final = "trim_bottom"

CONF_COLORS: Final = "colors"

CONF_ATTRIBUTES = "attributes"
CONF_AUTO_UPDATE = "auto_update"
CONF_AVAILABLE_API_DREAME = "dreame"
CONF_AVAILABLE_API_ROIDMI = "roidmi"
CONF_AVAILABLE_API_VIOMI = "viomi"
CONF_AVAILABLE_API_IJAI = "ijai"
CONF_AVAILABLE_API_XIAOMI = "xiaomi"
CONF_AVAILABLE_COUNTRIES = ["cn", "de", "us", "ru", "tw", "sg", "in", "i2"]
CONF_BOTTOM = "bottom"
CONF_COLOR = "color"
CONF_COLORS = "colors"
CONF_COUNTRY = "country"
CONF_DRAW = "draw"
CONF_FORCE_API = "force_api"
CONF_FONT = "font"
CONF_FONT_SIZE = "font_size"
CONF_LEFT = "left"
CONF_MAP_TRANSFORM = "map_transformation"
CONF_RIGHT = "right"
CONF_ROOM_COLORS = "room_colors"

CONF_DRAWABLES: Final = "drawables"
CONF_AVAILABLE_APIS = [
    CONF_AVAILABLE_API_XIAOMI,
    CONF_AVAILABLE_API_VIOMI,
    CONF_AVAILABLE_API_ROIDMI,
    CONF_AVAILABLE_API_DREAME,
    CONF_AVAILABLE_API_IJAI,
]

CONF_SIZES: Final = "sizes"

CONF_TEXTS: Final = "texts"
CONF_TEXT_VALUE: Final = "text"
CONF_TEXT_X: Final = "x"
CONF_TEXT_Y: Final = "y"
CONF_TEXT_COLOR: Final = "color"
CONF_TEXT_FONT: Final = "font"
CONF_TEXT_FONT_SIZE: Final = "font_size"
