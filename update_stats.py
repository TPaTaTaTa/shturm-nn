TEAM_URL = "https://futsal-nn.ru/team/1059741"

import urllib.request
import urllib.error

try:
    request = urllib.request.Request(
        TEAM_URL,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        print("Статус:", response.status)
        print("Получено байт:", len(response.read()))
except Exception as error:
    print("Ошибка:", error)
