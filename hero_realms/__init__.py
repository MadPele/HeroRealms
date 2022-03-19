from flask import Flask
from hero_realms.config import Config

app = Flask(__name__)
app.config.from_object(Config)

import hero_realms.views
