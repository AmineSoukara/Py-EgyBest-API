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
        self.refresh_token = None

        if id and password:
            self.access_token, self.refresh_token = self.get_tokens(id, password)
        else:
            self.access_token = access_token

    def format_api_url(self, url):
        if not re.match("(?:http|ftp|https)://", url):
            return "http://{}".format(url)
        return url

    def get_tokens(self, id, password):
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
            return x.data.access_token, x.data.refresh_token 
        else:
            raise LoginError(x.message)


    async def fetch(self, route, method="GET", timeout=30, **params):
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

        if not isinstance(version, int):
            raise ApiConnectionError(f"Version Arg Must Be A Number Not {type(version)}")

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

    async def movietable(self, url: str):
        """
        Returns An Object.
                Info: إستخراج كافة معلومات الفيلم مع روابط التحميل و المشاهدة
                Parameters:
                        url (str): Movie Link
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("movietable", url=url)



    async def quality(self, url: str):
        """
        Returns An Object.
                Info: إستخراج الجودة
                Parameters:
                        url (str): Link (Show - Movie ...)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("quality", url=url)

    async def rating_percent(self, url: str):
        """
        Returns An Object.
                Info: إستخراج التقيم
                Parameters:
                        url (str): Link (Show - Movie ...)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("rating_percent", url=url)

    async def note(self, url: str):
        """
        Returns An Object.
                Info: إستخراج الملاحظة
                Parameters:
                        url (str): Link (Show - Movie ...)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("note", url=url)


    async def is_page_unavailable(self, url: str):
        """
        Returns An Object.
                Info: عرض الصفحة اذا كانت غير متوفرة
                Parameters:
                        url (str): Link (Show - Movie ...)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("check_page", url=url)

    async def story(self, url: str):
        """
        Returns An Object.
                Info: إستخراج القصة
                Parameters:
                        url (str): Link (Show - Movie ...)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("story", url=url)

    async def trailer(self, url: str):
        """
        Returns An Object.
                Info: إستخراج التريلر 
                Parameters:
                        url (str): Link (Show - Movie ...)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("trailer", url=url)

    async def thumbnail(self, url: str):
        """
        Returns An Object.
                Info: إستخراج الصورة
                Parameters:
                        url (str): Link (Show - Movie ...)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("thumbnail", url=url)

    async def title(self, url: str):
        """
        Returns An Object.
                Info: إستخراج العنوان 
                Parameters:
                        url (str): Link (Show - Movie ...)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("title", url=url)

    async def similar(self, url: str):
        """
        Returns An Object.
                Info: إستخراج الافلام المتشابهة
                Parameters:
                        url (str): Link (Movie)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("similar", url=url)

    async def actors(self, url: str):
        """
        Returns An Object.
                Info: إستخراج معلومات الممثلين
                Parameters:
                        url (str): Link (Show - Movie ...)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("actors", url=url)


    async def search(self, query: str, type: str):
        """
        Returns An Object.
                Info: البحث المتطور
                Parameters:
                        query (str): title (Show - Movie ...) 
                        type (str): types (all-serie-movie-anime-show) default all 
               Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("search", query=query, type=type)


    async def pages(self, path: str, limit: int):
        """
        Returns An Object.
                Info: استخراج المعطيات من عدة صفحات من فرع محدد
                Parameters:
                        path (str): paths (movies/top - movies/latest ...)
                        limit (int): number of pages default 1 
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """

        if not isinstance(limit, int):
            raise ApiConnectionError(f"Limit Arg Must Be A Number Not {type(limit)}")

        return await self.fetch("pages", path=path, limit=limit)

    async def page(self, path: str, number: int):
        """
        Returns An Object.
                Info: استخراج المعطيات من صفحة محددة من فرع محدد
                Parameters:
                        path (str): paths (movies/top - movies/latest ...)
                        number (int): page number default 1 
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """

        if not isinstance(number, int):
            raise ApiConnectionError(f"Number Arg Must Be A Number Not {type(number)}")

        return await self.fetch("page", path=path, number=number)


    async def seasons(self, url: str):
        """
        Returns An Object.
                Info: إستخراج المواسم من مسلسل معين
                Parameters:
                        url (str): Link (Show - Serie)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("seasons", url=url)


    async def episodes(self, url: str):
        """
        Returns An Object.
                Info: إستخراج الحلقات من موسم معين
                Parameters:
                        url (str): Season Link (Show-Serie)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("episodes", url=url)

    async def previous_next(self, url: str):
        """
        Returns An Object.
                Info: إستخراج الحلقة السابقة و التالية لحلقة معينة
                Parameters:
                        url (str): Episode Link (Show-Serie)
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("previous_next", url=url)

    async def maintenance(self):
        """
        Returns An Object.
                Info: عرض إذا كان أيبي تحت الصيانة
                Parameters:
                        None
                Returns:
                        Result Object (str): Results Which You Can Access With Dot Notation
        """
        return await self.fetch("maintenance")
