# 🔐 Advanced Encryption Tool

COMPANY: CODTECH IT SOLUTION

NAME: SAKSHAM VIJAY KHOBRAGADE

INTERN ID: CT04DG2805

DOMAIN: CYBER SECURITY & ETHICAL HACKING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

A powerful, user-friendly GUI-based encryption and decryption tool built with Python. This application allows secure encryption and decryption of files using AES-256 encryption standard and password-based key derivation.

---

## 📌 Features

- ✅ **AES-256 Encryption** for strong, military-grade security.
- ✅ **GUI Interface** built with `tkinter` for easy usage.
- ✅ **Password Protection** using PBKDF2 HMAC SHA256.
- ✅ **Encrypted file output** with `.enc` extension.
- ✅ **Decrypted file output** with `.dec` extension.
- ✅ **Cross-platform compatible** (Windows/Linux/macOS).
- ✅ **Clean error handling** with user-friendly messages.

---

## 🧰 Technologies Used

- Python 3.x
- `tkinter` – for GUI
- `cryptography` – for encryption/decryption
- `os`, `base64`, `hashlib` – for file handling and security

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Sakshamk17/Advanced_encryption_tool.git
cd Advanced_encryption_tool
```

### 2. Install Dependencies

```bash
pip install cryptography
```

### 3. Run the App

```bash
python main.py
```

---

##  File Structure
Advanced_encryption_tool/
│
├── encryption_tool.py       # Core encryption/decryption logic
├── gui.py                   # GUI Interface using tkinter
├── main.py                  # Entry point to launch the app
├── utils.py                 # Helper utilities (e.g., key derivation)
├── test.txt                 # Sample input file
├── test.txt.enc             # Sample encrypted file (output)
├── test.txt.enc.dec         # Sample decrypted file (output)
├── README.md                # Project documentation
├── requirements.txt         # Optional: dependency list
└── __pycache__/             # Auto-generated Python cache (can be ignored)

---

## 📝 How to Use

### 🔐 Encrypting a File

Launch the app.

1.Click "Browse" to select a file.

2.Click "Encrypt" and enter a password.

3.A new file named yourfile.txt.enc is generated.

### 🔓 Decrypting a File

1.Click "Decrypt".

2.Select an encrypted .enc file.

3.Enter the correct password used during encryption.

4.A new file named yourfile.txt.enc.dec will be created.

---

## 🛡️ Security Notes

Uses AES-256 CBC mode for encryption.

Password-based key derivation via PBKDF2HMAC ensures strong keys.

Do not lose the password, as decryption without it is impossible.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## Outputs

![Image](https://github.com/user-attachments/assets/4646d78e-3a75-4e1f-8acc-90667832a574)

![Image](https://github.com/user-attachments/assets/6c7bd4e4-622a-4c87-9e66-4b0a9613279a)

![Image](https://github.com/user-attachments/assets/4b6550f3-3903-447f-ba2b-3ea0c4360550)

![Image](https://github.com/user-attachments/assets/53daef72-56dc-4a06-8010-55711f1b26b3)
