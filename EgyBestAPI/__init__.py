"""
Py-EgyBest-Api
~~~~~~~~~
:Copyright: (c) 2022 By Amine Soukara <https://github.com/AmineSoukara>.
:License: MIT, See LICENSE For More Details.
:Link: https://github.com/AmineSoukara/Py-EgyBest-Api
:Description: Asynchronous Python Wrapper For EgyBest-API.
"""


import re
from asyncio.exceptions import TimeoutError
from json.decoder import JSONDecodeError

import requests
from dotmap import DotMap
from requests.exceptions import ConnectionError
from urllib3.exceptions import MaxRetryError, NewConnectionError

# from requests.exceptions import JSONDecodeError


class InvalidAccessToken(Exception):
    pass


class RateLimitExceeded(Exception):
    pass


class UserBanned(Exception):
    pass


class LoginError(Exception):
    pass


class ApiConnectionError(Exception):
    pass


class RaEye:
    """
    RaEye Class To Access All The Endpoints Of API.
    ___________
    Parameters:
        RaEye(API_URL: str, ACCESS_TOKEN: str)
    """

    def __init__(
        self, api_url: str, id: int = None, password: str = None, access_token: str = ""
    ):
        self.api_url = self.format_api_url(api_url.strip(" /"))
        if id and password:
            self.access_token = self.get_access_token(id, password)
        else:
            self.access_token = access_token

    def format_api_url(self, url):
        if not re.match("(?:http|ftp|https)://", url):
            return "http://{}".format(url)
        return url

    def get_access_token(self, id, password):
        try:
            body = {"id": id, "password": password}

            url = f"{self.api_url}/login/app"
            resp = requests.post(url, json=body, timeout=15)

            if resp.status_code == 403:
                raise UserBanned("Congrats, Your Are Banned (Forever)")

            response = resp.json()

        except (
            TimeoutError,
            ConnectionError,
            MaxRetryError,
            NewConnectionError,
            JSONDecodeError,
        ):
            raise ApiConnectionError("Failed To Communicate With RaEye Server.")

        x = DotMap(response)
        if x.success:
            return x.data.access_token
        else:
            raise LoginError(x.message)

    async def fetch(self, route, method="GET", timeout=60, **params):
        try:
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.access_token,
            }

            url = f"{self.api_url}/{route}"
            resp = requests.request(
                method, url, headers=headers, timeout=timeout, params=params
            )

            if resp.status_code in (422, 401):
                raise InvalidAccessToken(
                    "Invalid Access Token, Get An Access Token From @EgyBestAPIBot"
                )
            elif resp.status_code == 429:
                raise RateLimitExceeded("Rate Limit Exceeded")
            elif resp.status_code == 403:
                raise UserBanned("Congrats, Your Are Banned (Forever)")

            response = resp.json()

        except (
            TimeoutError,
            ConnectionError,
            MaxRetryError,
            NewConnectionError,
            JSONDecodeError,
        ):
            raise ApiConnectionError("Failed To Communicate With RaEye Server.")

        return DotMap(response)

    async def dls(self, url: str, version: int):
        """
        Returns An Object.
                Info: إستخراج روابط التحميل و المشاهدة
                Parameters:
                        url (str): Episode or Movie link
                        version (int): 1,2 Return As list 3,4 As Dict, Default 1 
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("dls", url=url, v=version)


    async def info(self, url: str):
        """
        Returns An Object.
                Info: إستخراج كافة المعلومات
                Parameters:
                        url (str): Link (Show - Movie ...)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("info", url=url)

    async def table(self, url: str):
        """
        Returns An Object.
                Info: إستخراج المعلومات
                Parameters:
                        url (str): Link (Show - Movie ...)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("table", url=url)
