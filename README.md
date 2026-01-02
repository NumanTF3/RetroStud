# RetroStud

**RetroStud** is a Python-based Roblox launcher designed to **preserve, revive, and make playable old Roblox clients**.
It enables users to host or join experiences from classic Roblox eras with minimal setup, either locally or online.

---

## Project Vision

RetroStud exists to:

* Preserve old Roblox clients and gameplay
* Allow free experimentation without modern restrictions
* Let users relive Roblox nostalgia
* Make old Roblox playable again with minimal effort

---

## What is RetroStud?

RetroStud is a **standalone Roblox launcher and server system** written in **pure Python**.

It allows users to:

* Run old Roblox clients
* Host servers
* Join games with custom settings
* Play freely without official Roblox services

RetroStud supports both **LAN** and **online play**, giving users full control over their experience.

---

## Features

* Support for **Roblox clients from 2008M to 2022M**
* Play **any `.rbxl` Roblox map**
* Join with **any username**
* **No chat filtering**
* Fully featured **avatar editor**

  * Body colors
  * Faces
  * Shirts, pants, hats
  * Bundles and catalog items
* Choose between **R6** and **R15** body types
* Optional **Filtering Enabled toggle**

  * Disabled mode allows stronger exploits
* Map editing using **Roblox Studio 2022**
* Works over:

  * Local Area Network (LAN)
  * Online connections (via **Radmin VPN** or **playit.gg**)
* Can function as:

  * Standalone server
  * Client only
  * Server + client

---

## Supported Clients

* **2008**
* **2013**
* **2014**
* **2015**
* **2016**
* **2017**
* **2018**
* **2019**
* **2020**
* **2021**
* **2022**

---

## Developers

* **Guest 43854 / Matthew** — Project Owner
* **Numan** — Lead Developer

---

## Community

Join the official Discord server for support, updates, and discussion:

👉 **[https://discord.gg/Wjha2YB33P](https://discord.gg/Wjha2YB33P)**

---

## Build & Compile Guide

### Clone the Repository

```bash
git clone https://github.com/NumanTF3/RetroStud/
cd RetroStud
```

---

### Windows (Recommended)

Run the provided build script:

```bat
compile.bat
```

The compiled executable will appear in the `dist` folder.

---

### Manual Build (All Platforms)

1. Install **Python**
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Compile using PyInstaller:

```bash
pyinstaller --noconsole --onefile --windowed --icon=Logo.ico --add-data "Logo.ico;." "retrostud.py"
```

4. The output executable will be located in:

```
dist/
```

---

## Disclaimer

RetroStud is an **independent preservation project**.
It is **not affiliated with Roblox Corporation**.

This project is intended for **educational, archival, and experimental use**.

---

## Permissions

You are permitted to:

* Use this project freely
* Fork the repository
* Modify the source code
* Redistribute modified or unmodified versions
* Use the project for personal or public servers

---

## Conditions

The following conditions **must be met**:

1. **Credit is required**

   * You must credit:

     * The original RetroStud repository
     * The original developers (Guest 43854 / Matthew and Numan)

2. **Preservation intent**

   * Forks and derivatives must not remove or misrepresent the project’s primary goal:

     * Preserving old Roblox clients
     * Allowing free experimentation
     * Enabling nostalgic experiences
     * Making old Roblox playable easily

3. **No ownership claims**

   * You may not claim RetroStud as entirely your own work.

---

## Restrictions

* This project may not be used to impersonate Roblox Corporation
* This project may not be sold as an official Roblox product

---

## Disclaimer of Warranty

This software is provided **“as is”**, without warranty of any kind.
The authors are not responsible for any damage or misuse.
