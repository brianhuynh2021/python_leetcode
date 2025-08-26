#!/usr/bin/env python3
import base64, hashlib, hmac, json, struct, time, urllib.request

API_URL = "https://api.challenge.hennge.com/challenges/backend-recursion/004"
TIME_STEP = 30
DIGITS = 10
SUFFIX = "HENNGECHALLENGE004"

def totp_sha512(secret: bytes) -> str:
    counter = int(time.time()) // TIME_STEP
    msg = struct.pack(">Q", counter)
    hs = hmac.new(secret, msg, hashlib.sha512).digest()
    offset = hs[-1] & 0x0F
    dbc = ((hs[offset] & 0x7F) << 24) | ((hs[offset+1]&0xFF) << 16) | ((hs[offset+2]&0xFF) << 8) | (hs[offset+3]&0xFF)
    code = dbc % (10 ** DIGITS)
    return str(code).zfill(DIGITS)

def main():
    email = "huynh2102@gmail.com"
    gist_url = "https://gist.github.com/brianhuynh2021/86316ddbf940034c5f238137b11b495b"

    secret = (email + SUFFIX).encode("ascii")
    otp = totp_sha512(secret)

    payload = {
        "github_url": gist_url,
        "contact_email": email,
        "solution_language": "python"
    }
    body = json.dumps(payload).encode("utf-8")

    auth = base64.b64encode(f"{email}:{otp}".encode()).decode()
    req = urllib.request.Request(API_URL, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", "Basic " + auth)

    with urllib.request.urlopen(req) as resp:
        print(resp.status, resp.read().decode())

if __name__ == "__main__":
    main()