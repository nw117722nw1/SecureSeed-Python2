import os, time, psutil, random, base64, uuid, hashlib, getpass

def generate_secure_seed(bits=512, count=1):
    """
    توليد Seeds عالية العشوائية باستخدام 10 مصادر Entropy.
    bits: طول المفتاح (512 افتراضيًا)
    count: عدد الـSeeds
    """
    if bits not in [128, 256, 512]:
        raise ValueError("الطول يجب أن يكون 128 أو 256 أو 512 بت")

    seeds = []
    for _ in range(count):
        # 10 مصادر مختلفة
        parts = [
            str(time.time_ns()),                         # 1- وقت نانوثانية
            str(time.perf_counter_ns()),                 # 2- Performance Counter
            str(psutil.cpu_percent()),                   # 3- نسبة استخدام CPU
            str(psutil.virtual_memory().available),      # 4- الذاكرة المتاحة
            os.urandom(32).hex(),                        # 5- بايتات عشوائية من النظام
            str(uuid.getnode()),                         # 6- MAC Address
            str(os.getpid()),                            # 7- معرّف العملية
            getpass.getuser(),                           # 8- اسم المستخدم
            str(random.randint(0, 999999999)),           # 9- رقم عشوائي إضافي
            str(int(time.time() * 1000))                 # 10- الوقت بالمللي ثانية
        ]

        # تحويل النصوص إلى Bytes
        raw = "|".join(parts).encode()

        # تجزئة حسب الطول
        if bits == 128:
            digest = hashlib.md5(raw).digest()
        elif bits == 256:
            digest = hashlib.sha256(raw).digest()
        else:
            digest = hashlib.sha512(raw).digest()

        # ترميز Base64
        seeds.append(base64.b64encode(digest).decode())

    return seeds
