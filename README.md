```markdown
# VANET Secure Routing Protocol Simulation (Python)

This project implements a **secure routing protocol for Vehicular Ad Hoc Networks (VANET)** using **hash functions** and **digital signatures**. The simulation is written entirely in **Python**, making it a lightweight, accessible alternative to NS-2, NS-3, or OMNeT++.

> 🔐 This project simulates and defends against attacks such as **data tampering** and **impersonation/spoofing**, using cryptographic verification.

---

## 📁 Project Structure

```

.
├── vehicles.py         # Vehicle logic, hashing, signing, and signature verification
├── simulation.py      # Main simulation: movement, message passing, and attacks
├── plot.py             # Hash time visualization
├── results/            # Auto-generated outputs (CSV & plots)
└── README.md           # You're reading it

```

---

## 🚗 Features

- 🔑 **Digital Signatures (RSA)** for message authentication
- 🧾 **SHA256 Hashing** with salt to ensure message integrity
- ⚠️ Simulated **Tampering and Spoofing Attacks**
- 📊 **Hash Time Measurement** with plotting via `matplotlib`
- ✅ **Signature Verification** using sender’s public key
- 📂 Organized code for easy understanding and extension

---

## 🔧 Requirements

Install dependencies using pip:

```bash
pip install cryptography pandas matplotlib
````

---

## ▶️ How to Run

### 1. Run the simulation:

```bash
python simulations.py
```

* Simulates 20 steps of vehicle communication
* Logs:

  * Message signature verification
  * Attack detection (tampering and spoofing)
* Outputs hash timings in `results/hash_times.csv`

### 2. Plot hash generation times:

```bash
python plot.py
```

* Loads data from `results/hash_times.csv`
* Saves plot as `results/hash_plot.png`
* Displays line graph of hash time per message

---

## 🧪 Attack Scenarios Simulated

### 🔁 Message Tampering

At step 10, the message from Vehicle V1 is tampered (speed is altered). The receiver detects invalid signature.

### 👤 Impersonation/Spoofing

At step 15, a new vehicle (`Attacker`) signs a message pretending to be V1. The verification fails due to mismatched key.

---

## 📊 Sample Output

```
Step 10: Message from V1 verified by V2: True
[!] Simulating Tampering Attack...
Tampered message: Verified? False

Step 15: Message from V1 verified by V2: True
[!] Simulating Spoofing Attack...
Spoofed message pretending to be V1: Verified? False
```

---

## 📌 Notes

* The system assumes public key distribution is already done (pre-loaded).
* For real-world scenarios, a PKI or blockchain-based registry can be used.
* RSA 2048-bit is used for digital signatures, ensuring strong security.

---

## 🥇 Why This Project Stands Out

* ✅ No need for complex simulation tools (NS-2/NS-3/OMNeT++)
* ✅ Demonstrates **core security principles**
* ✅ Modular, readable, and **easy to extend**
* ✅ Ready for evaluation in internships or academic submissions

---

## 📞 Contact

Author: *Mohd Abubakar*
Email: *mohdabubakar477@gmail.com*
GitHub: *[https://github.com/Muhd-Abubakar/]*
