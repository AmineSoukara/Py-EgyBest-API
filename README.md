![RUN](https://telegra.ph/file/39890dfb899f4a943e626.jpg)

<div align="center">

> Asynchronous Python Wrapper For EgyBest-API.

<!-- Badges -->
<p>
  <a href="https://github.com/AmineSoukara/Py-EgyBest-Api/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/aminesoukara/Py-EgyBest-Api" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/aminesoukara/Py-EgyBest-Api" alt="last update" />
  </a>
  <a href="https://github.com/AmineSoukara/Py-EgyBest-Api/network/members">
    <img src="https://img.shields.io/github/forks/aminesoukara/Py-EgyBest-Api" alt="forks" />
  </a>
  <a href="https://github.com/AmineSoukara/Py-EgyBest-Api/stargazers">
    <img src="https://img.shields.io/github/stars/aminesoukara/Py-EgyBest-Api" alt="stars" />
  </a>
  <a href="https://github.com/AmineSoukara/Py-EgyBest-Api/issues/">
    <img src="https://img.shields.io/github/issues/aminesoukara/Py-EgyBest-Api" alt="open issues" />
  </a>
  <a href="https://github.com/AmineSoukara/Py-EgyBest-Api/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/aminesoukara/Py-EgyBest-Api.svg" alt="license" />
  </a>
  <a href="https://pepy.tech/project/Py-EgyBest-Api">
    <img src="https://static.pepy.tech/personalized-badge/py-egyBest-api?period=total&units=none&left_color=grey&right_color=red&left_text=Total-Downloads" alt="Total Downloads" />
  </a>
  <a href="https://github.com/AmineSoukara/Py-EgyBest-API">
    <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FAmineSoukara%2FPy-EgyBest-API&count_bg=%23FF0000&title_bg=%23555555&icon=tinder.svg&icon_color=%23FF0000&title=Hits&edge_flat=false" alt="hits" />
  </a>
</p>



<h4>
    <a href="https://github.com/AmineSoukara/EgyBest-Api">API Repository</a>
  <span> · </span>
    <a href="https://github.com/AmineSoukara/Py-EgyBest-Api">Documentation</a>
  <span> · </span>
    <a href="https://github.com/AmineSoukara/Py-EgyBest-Api/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/AmineSoukara/Py-EgyBest-Api/issues/">Request Feature</a>
  </h4>
</div>

##

<div align="center">

# ⚠️ Note:
- For Personal Use Only, Don't Create Or Build Something Huge With This API Without Permission Otherwise You Will Be Banned
- This Project Is Licensed Under The [MIT License](https://github.com/AmineSoukara/Py-EgyBest-Api/blob/main/LICENSE)

##

# 🔐 Requirements:

- Python 3.8 Or Newer.
- API URL and Access Token From :
<a href="https://t.me/EgyBestAPIBot"><img src="https://img.shields.io/badge/@EgyBestAPIBot-FFFF00?style=flat&logo=telegram&logoColor=white?logoWidth=100"></a>

##

# 🗜 Installation:

```sh
$ pip3 install Py-EgyBest-Api
```
##

# ❓ Usage:
For Example, To Get Direct Links, You Can Do This
<div align="left">

```py
from EgyBestAPI import RaEye
from asyncio import run

API = "http://0.1.2.3" # Required
TOKEN = "abcd" # Required 
ID = None # Optional 
PASSWORD = None # Optional

x = RaEye(API, access_token=TOKEN, id=ID, password=PASSWORD)

async def main():
    z = await x.dls(url="https://www.egybest.org/movie/top-five-2014", version=2)

    print(z)
    # output: DotMap(a=1, b=2)
    print(z.type)
    # output: movie

    print(z.toDict())
    # output: {'a': 1, 'b': 2}
    print(z["type"])
    # output: movie

    # To Print Results As Json
    z.pprint(pformat='json')
    # output: {...}

run(main())
```

<div align="center">

##

# 🪐 Documentation:
There Is No Documentation, But You Can Take Help From The DocStrings :

<div align="left">

```py
from EgyBestAPI import RaEye

print(help(RaEye.dls))
```

<div align="center">

##

# ⭐️ Features:
<div align="left">

* [x] Smart Search
* [x] Extract Full Info From Url (Movie-Serie/Anime)
* [x] Extract: Story - Image - Title - Trailer - Actors Info - Note
* [x] Extract Download and Stream Links With Full Info
* [x] Extract Similar Movies
* [x] Extract Seasons / Episodes
* [x] Extract Previous And Next Episode
* [x] Extract Movies Or Series From Paths
* [x] And More ...

<div align="center">

##

# 🧭 RoadMap:
<div align="left">

* [ ] Todo

<div align="center">

##

# 👨‍💻 Dev & Support:
<a href="https://bio.link/aminesoukara"><img src="https://img.shields.io/badge/@AmineSoukara-000000?style=flat&logo=messenger&logoColor=white?logoWidth=100"></a>
<a href="https://t.me/EgyBestBotSupport"><img src="https://img.shields.io/badge/Group-FF0000?style=flat&logo=telegram&logoColor=white?logoWidth=100"></a>
<a href="https://t.me/EgyBestBotOriginal"><img src="https://img.shields.io/badge/Channel-FF0000?style=flat&logo=telegram&logoColor=white?logoWidth=100"></a>

##

# 📭 Credits:
<a href="https://github.com/AmineSoukara/EgyBest-Api"><img src="https://img.shields.io/badge/@EgyBest–API-FE9A2E?style=flat&logo=github&logoColor=black"></a>

##

# 🌍 Contributing:

<a href="https://github.com/AmineSoukara/Py-EgyBest-Api/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=aminesoukara/Py-EgyBest-Api" />
</a>

Contributions Are Always Welcome!
See `contributing.md` For Ways To Get Started.

##

![⭐️](https://telegra.ph/file/b132a131aabe2106bd335.gif)
