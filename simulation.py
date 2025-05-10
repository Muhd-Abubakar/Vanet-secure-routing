from vehicles import Vehicle
import time
import pandas as pd
import os

def simulate():
    if not os.path.exists("results"):
        os.makedirs("results")

    v1 = Vehicle("BMW", 50, (0, 0))
    v2 = Vehicle("AUDI", 40, (100, 100))
    hash_times = []

    for step in range(20):
        v1.move(0.1)
        v2.move(0.1)

        msg = v1.generate_message()
        t1 = time.time()
        hash_val = v1.hash_message(msg)
        t2 = time.time()

        signature = v1.sign_message(msg)

        verified = v2.verify_signature(msg, signature, v1.public_key)
        print(f"Step {step}: Message from {v1.id} verified by {v2.id}: {verified}")
        hash_times.append(t2 - t1)

        # Tampering attack
        if step == 10:
            print("\n[!] Simulating Tampering Attack...")
            tampered_msg = msg.copy()
            tampered_msg["speed"] = 999
            is_valid = v2.verify_signature(tampered_msg, signature, v1.public_key)
            print(f"Tampered message: Verified? {is_valid}\n")

        # Spoofing attack
        if step == 15:
            print("\n[!] Simulating Spoofing Attack...")
            attacker = Vehicle("Attacker", 80, (200, 200))
            fake_msg = v1.generate_message()  # Pretend to be V1
            fake_signature = attacker.sign_message(fake_msg)
            is_valid = v2.verify_signature(fake_msg, fake_signature, v1.public_key)
            print(f"Spoofed message pretending to be {v1.id}: Verified? {is_valid}\n")

    # Save hash times for plotting
    df = pd.DataFrame({"hash_time": hash_times})
    df.to_csv("results/hash_times.csv", index=False)

if __name__ == "__main__":
    simulate()
