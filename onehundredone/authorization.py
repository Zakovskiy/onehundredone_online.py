import base64
import hashlib
from datetime import datetime
from .utils import objects


class Authorization:

    def __init__(self, client) -> None:
        self.client = client

    def get_session_key(self) -> objects.GetSessionKey:
        data = {
            "command": "c",
            "l": "ru",
            "tz": "+02:00",
            "t": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z",
            "pl": self.client.pl,
            "p": 13,
        }
        if self.client.pl == "ios":
            data.update({
                "v": "1.3.2",
                "ios": "14.4",
                "d": "iPhone8,4",
                "n": "101.ios",
            })
        else:
            data.update({
                "v": "1.3.2",
                "d": "xiaomi cactus",
                "and": 28,
                "n": f"101.{self.client.pl}",
            })
        self.client.send_server(data)
        data = self.client._get_data("sign")
        return data["key"]

    def sign(self, key: str) -> dict:
        hash = base64.b64encode(hashlib.md5((f"{key}fnd;vnbwk;vb ejkwfkjew fwek fewkj fjekw; f;kao oboiboniuj").encode()).digest()).decode()
        self.client.send_server(
            {
                "command": "sign",
                "hash": hash,
            }
        )
        return self.client.listen()

    def signin_by_access_token(self, token: str) -> int:
        self.client.token = token
        self.client.send_server(
            {
                "command": "auth",
                "token": self.client.token,
            }
        )
        authorized = self.client._get_data("authorized")
        if authorized["command"] == "err":
            raise objects.Err(authorized)
        self.client.uid = authorized["id"]
        self.client.logger.debug(f"{self.client.tag}: Success auth")
        data = self.client._get_data("uu")
        while data["k"] != "dtp":
            if data.get("v"):
                self.client.info[data["k"]] = data["v"]
            data = self.client._get_data("uu")
        return authorized["id"]

    def google_auth(self, id_token: str) -> dict:
        self.client.send_server(
            {
                "command": "101_google_auth",
                "id_token": id_token,
            }
        )
        return self.client.listen()

    def get_captcha(self) -> dict:
        self.client.send_server(
            {
                "command": "get_captcha",
            }
        )
        return self.client._get_data("captcha")

    def register(self, name, captcha: str = '') -> objects.Register:
        self.client.send_server(
            {
                "command": "register",
                "name": name,
                "captcha": captcha,
            }
        )
        return objects.Register(self.client._get_data("set_token")).Register