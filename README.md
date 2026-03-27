# OnlyFlags Dreamworks CTF

## Running the challenge locally

```bash
docker run -d -p 5000:5000 --name ctf-challenge rayyjr/onlyflags-dreamworks-challenge:latest
```
Surf to localhost:5000/

## The Challenge

We exiled someone from Team OnlyFlags and that person might have left traces which may or may not lead to unauthorised access. Look around and find out if you can still get access to our super secure website.

## Hints

- **Reading** will help you a lot throughout this CTF
- Listening might aid you in obtaining a key
- Keep it simple and stick to what you know

## Documentation

### 1. Docker

Our application runs inside of a docker container

### 2. Frontend

We vibecoded the HTML and CSS

### 3. Backend

We used Python to manage the backend which routes you to the specific HTML pages. We also used Python to validate the username and password.

### Modules

- hashlib
- base64
- os
- flask
- dotenv

### 4. Structure
```
OnlyFlags/
├── static/
│   ├── audio/
│   │   └── audio_x.wav
│   ├── images/
│   │   ├── onlyflags_logo.png
│   │   └── [backgrounds, cards, and media assets]
│   └── style.css
├── templates/
│   ├── acces_denied.html
│   ├── blog.html
│   ├── blog_[user].html  # (alex, hiccup, po, shrek, hidden)
│   ├── home.html
│   ├── login.html
│   ├── robots.html
│   └── studiomaster.html
├── app.py
├── auth.py
├── Dockerfile
├── README.md
└── requirements.txt
```



## How To Solve 101

1. Recon and steganography: Surf to /robots.txt, here you will find an image with the filepath for the admin login page hidden in the metadata (exiftool).

2. OSINT: Check the blog pages for a certain name using the hints and try to find that person's blog post. On that page you will see a base64 string.

3. Audio analysis: You will find an audio file that you will have to analyze. This will give you the XOR key.

4. Decryption: Decode from base64, XOR that output using the given key and finally use ROT13 to obtain the username and password.

5. Go to the admin page and login to receive the key.
