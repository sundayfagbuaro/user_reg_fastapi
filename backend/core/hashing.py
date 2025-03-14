from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod        # This second staticmethod would be used to get password hash
    def get_password_hash(password):        # The password here is the original plain_password
        return pwd_context.hash(password)
