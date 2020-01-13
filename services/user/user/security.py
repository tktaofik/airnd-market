from passlib.hash import argon2

salt = "airnd-market.user"
pwd_hash = argon2.using(salt=salt.encode())


def hashPassword(pwd):
    return pwd_hash.hash(pwd)


def verifyPassword(pwd, hash):
    return pwd_hash.verify(pwd, hash)
