import random
import hashlib
import time
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature

class Vehicle:
    """
    Represents a vehicle in the VANET (Vehicular Ad Hoc Network) system.
    Each vehicle has a unique ID, speed, position, and cryptographic keys for secure communication.
    """
    
    def __init__(self, vehicle_id, speed, position):
        """
        Initializes a Vehicle object with the given ID, speed, and position.
        Generates a unique salt and RSA key pair for the vehicle.
        """
        self.id = vehicle_id  # Unique identifier for the vehicle
        self.speed = speed  # Speed of the vehicle
        self.position = list(position)  # Current position of the vehicle as a list [x, y]
        self.salt = "vanet" + str(random.random())  # Random salt for hashing
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)  # RSA private key
        self.public_key = self.private_key.public_key()  # Corresponding RSA public key

    def move(self, dt):
        """
        Updates the vehicle's position based on its speed and a random factor.
        :param dt: Time interval for the movement.
        """
        self.position[0] += self.speed * dt * random.uniform(0.8, 1.2)  # Update x-coordinate
        self.position[1] += self.speed * dt * random.uniform(0.8, 1.2)  # Update y-coordinate

    def generate_message(self):
        """
        Generates a message containing the vehicle's ID, speed, and position.
        :return: A dictionary representing the message.
        """
        msg = {
            "vehicle_id": self.id,
            "speed": self.speed,
            "position": tuple(self.position),  # Convert position to a tuple for immutability
        }
        return msg

    def hash_message(self, message):
        """
        Computes a SHA-256 hash of the given message combined with the vehicle's salt.
        :param message: The message to be hashed.
        :return: The hexadecimal representation of the hash.
        """
        data = str(message).encode() + self.salt.encode()  # Combine message and salt
        return hashlib.sha256(data).hexdigest()  # Compute and return the hash

    def sign_message(self, message):
        """
        Signs the given message using the vehicle's private RSA key.
        :param message: The message to be signed.
        :return: The digital signature of the message.
        """
        # Create a digital signature using the private key
        data = str(message).encode()  # Encode the message as bytes
        signature = self.private_key.sign(
            data,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return signature

    def verify_signature(self, message, signature, public_key):
        """
        Verifies the digital signature of a message using the provided public RSA key.
        :param message: The original message.
        :param signature: The digital signature to verify.
        :param public_key: The public RSA key used for verification.
        :return: True if the signature is valid, False otherwise.
        """
        try:
            public_key.verify(
                signature,
                str(message).encode(),
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256()
            )
            return True  # Signature is valid
        except InvalidSignature:
            return False  # Signature is invalid
