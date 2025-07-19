import os, time, uuid, psutil, base64, hashlib, random, getpass, os as system_os


def generate_secure_seed(bits=256, count=1):
    if bits not in (128, 256, 512):
        raise ValueError("Bits must be 128, 256, or 512")

    seeds = []

    for _ in range(count):
        # 1) High-resolution time (nanoseconds)
        time1 = str(time.time_ns())

        # 2) Perf counter time
        time.sleep(random.uniform(0.001, 0.015))
        time2 = str(time.perf_counter_ns())

        # 3) CPU load
        cpu = str(psutil.cpu_percent(interval=0.05))

        # 4) Available RAM
        ram = str(psutil.virtual_memory().available)

        # 5) Cryptographically secure random bytes (32 bytes)
        rand_bytes = os.urandom(32).hex()

        # 6) MAC Address
        mac = uuid.getnode()

        # 7) PID
        pid = str(system_os.getpid())

        # 8) Username
        user = getpass.getuser()

        # 9) Random integer
        rand_int = str(random.randint(0, 999999999))

        # 10) Additional epoch timestamp (ms)
        epoch_ms = str(int(time.time() * 1000))

        # Combine all sources
        raw_seed = f"{time1}|{time2}|{cpu}|{ram}|{rand_bytes}|{mac}|{pid}|{user}|{rand_int}|{epoch_ms}".encode()

        # Hash based on length
        if bits == 128:
            digest = hashlib.md5(raw_seed).digest()
        elif bits == 256:
            digest = hashlib.sha256(raw_seed).digest()
        else:
            digest = hashlib.sha512(raw_seed).digest()

        seeds.append(base64.b64encode(digest).decode())

    return seeds


if __name__ == "__main__":
    for s in generate_secure_seed(512, 5):
        print(s)

