import requests
from loguru import logger


def request_harvester(
    method: str,
    url: str,
    headers: dict | None = None,
    data: dict | None = None,
    json: dict | None = None,
    cookies: dict | None = None,
    params: dict | None = None,
    files=None,
    session_name=requests.Session(),
    proxy_less=True,
):
    while True:
        try:

            if proxy_less is True:
                # logger.info("sending request proxyless")
                if method == "post":
                    response = session_name.post(
                        url,
                        headers=headers,
                        data=data,
                        json=json,
                        cookies=cookies,
                        files=files,
                        params=params,
                    )

                else:
                    response = session_name.get(
                        url,
                        headers=headers,
                        data=data,
                        cookies=cookies,
                        files=files,
                        params=params,
                    )
            if response.status_code == 200:
                # logger.info(f"{url} succesffully {method}")
                return {"response": response, "session": session_name}
            elif response.status_code == 404:
                logger.warning(f"Page not load {url} ({response.status_code})")
            else:
                logger.error(f"Request error : {response.status_code}")
                print(response.text)

                proxy_less = False

        except Exception as e:
            logger.debug(e)
