PORT = 8080  # Render thường mở cổng 8080 hoặc PORT do hệ thống gán qua biến môi trường

# name -> secret (32 hex chars)
USERS = {
    "tg": "e7d9f3a2b47c6e54aa12cc8890ed3a74",
}

MODES = {
    "classic": False,
    "secure": False,
    "tls": True
}

# BẮT BUỘC phải khai báo nếu bật chế độ TLS
TLS_DOMAIN = "www.google.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"
