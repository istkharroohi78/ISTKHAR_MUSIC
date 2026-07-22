from ISTKHAR_MUSIC.core.bot import ISTKHAR
from ISTKHAR_MUSIC.core.dir import dirr
from ISTKHAR_MUSIC.core.git import git
from ISTKHAR_MUSIC.core.runtime_patches import apply_runtime_patches
from ISTKHAR_MUSIC.core.userbot import Userbot
from ISTKHAR_MUSIC.misc import dbb, heroku
from ISTKHAR_MUSIC.security import drop_sensitive_env_vars

from .logging import LOGGER

dirr()
git()
dbb()
heroku()
apply_runtime_patches()

app = ISTKHAR()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

_removed_sensitive_env = drop_sensitive_env_vars()
if _removed_sensitive_env:
    LOGGER(__name__).info(
        "Security hardening active: stripped %s sensitive env vars from process environment.",
        len(_removed_sensitive_env),
    )
