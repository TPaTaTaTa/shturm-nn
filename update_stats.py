
import urllib.request
import urllib.error

urls = {
    "FUTSAL-NN": "https://futsal-nn.ru/team/1059741",
    "Проверка интернета": "https://example.com/",
}

for name, url in urls.items():
    print(f"\nПроверяем: {name}")

    try:
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "text/html",
            },
        )

        with urllib.request.urlopen(
            request, timeout=15
        ) as response:
            print("HTTP:", response.status)
            print("Байт:", len(response.read()))

    except urllib.error.HTTPError as error:
        print("HTTP ошибка:", error.code)

    except Exception as error:
        print("Ошибка соединения:", error)
