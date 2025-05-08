# 🔗 URL Shortener Tool (Python)

This repository contains my code for a simple but powerful **URL Shortener** I built with Python using the `pyshorteners` library. It allows you to convert long and messy URLs into shorter, cleaner links using the TinyURL service.

## 🚀 Features

- ✅ Shortens long URLs quickly
- ✅ Uses the `pyshorteners` library
- ✅ Simple and beginner-friendly code
- ✅ Lightweight and easy to expand or integrate

## 🛠️ Requirements

Make sure you have Python installed on your system. You also need to install the `pyshorteners` package.

```bash
pip install pyshorteners
```

## 🔧 Tech Stack:
- Language: Python
- Library: pyshorteners

## 💡 Features:
✅ Takes user input for any long URL
✅ Converts it into a compact, shortened link using TinyURL
✅ Lightweight and easy to integrate into larger applications

## 📂 Sample Code:
```bash
import pyshorteners

url = input("Enter URL to shorten:\n")
shortener = pyshorteners.Shortener()
print("New URL:", shortener.tinyurl.short(url))
```

## 🧠 How It Works
- The program prompts the user to input a long URL.
- It uses the TinyURL service via the pyshorteners library to generate a shortened link.
- It displays the new, shortened URL to the user.

## 🧪 Usage
```bash
python url_shortener.py
```

### Example
```bash
Enter URL to shorten:
https://github.com/isiaq-ibrahim
New URL: https://tinyurl.com/2345v7dw
```

### 📄 License

This project is open-source and free to use under the MIT License.

### 🙌 Contributing

Pull requests are welcome! If you'd like to improve the tool or add features, feel free to fork the repo and submit a PR.

### 📬 Contact

If you have any questions or want to connect, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/isiaq-ibrahim-468588156/).
