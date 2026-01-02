import os
import subprocess
import random
import glob
import atexit
import tkinter as tk
import configparser
import re
import shutil
import customtkinter as ctk
from tkinter import PhotoImage
from tkinter import ttk, filedialog, messagebox

BASE_DIR = os.getcwd()
CLIENTS_DIR = os.path.join(BASE_DIR, "Clients")
SHARED_DIR = os.path.join(BASE_DIR, "shared")
WEB_START_BAT = os.path.join(BASE_DIR, "Webserver", "Start.bat")
WEB_KILL_BAT = os.path.join(BASE_DIR, "Webserver", "Kill.bat")
SETTINGS_DIR = os.path.join(BASE_DIR, "Settings")

# Launch webserver ONCE
webserver_proc = None
if os.path.exists(WEB_START_BAT):
    webserver_proc = subprocess.Popen([WEB_START_BAT], shell=True)
atexit.register(lambda: subprocess.Popen([WEB_KILL_BAT], shell=True) if os.path.exists(WEB_KILL_BAT) else None)

ROBLOX_COLORS = [
    ("White", (242, 243, 243)),
    ("Grey", (161, 165, 162)),
    ("Light yellow", (249, 233, 153)),
    ("Brick yellow", (215, 197, 154)),
    ("Light green (Mint)", (194, 218, 184)),
    ("Light reddish violet", (232, 186, 200)),
    ("Pastel Blue", (128, 187, 219)),
    ("Light orange brown", (203, 132, 66)),
    ("Nougat", (204, 142, 105)),
    ("Bright red", (196, 40, 28)),
    ("Med. reddish violet", (196, 112, 160)),
    ("Bright blue", (13, 105, 172)),
    ("Bright yellow", (245, 205, 48)),
    ("Earth orange", (98, 71, 50)),
    ("Black", (27, 42, 53)),
    ("Dark grey", (109, 110, 108)),
    ("Dark green", (40, 127, 71)),
    ("Medium green", (161, 196, 140)),
    ("Lig. Yellowich orange", (243, 207, 155)),
    ("Bright green", (75, 151, 75)),
    ("Dark orange", (160, 95, 53)),
    ("Light bluish violet", (193, 202, 222)),
    ("Transparent", (236, 236, 236)),
    ("Tr. Red", (205, 84, 75)),
    ("Tr. Lg blue", (193, 223, 240)),
    ("Tr. Blue", (123, 182, 232)),
    ("Tr. Yellow", (247, 241, 141)),
    ("Light blue", (180, 210, 228)),
    ("Tr. Flu. Reddish orange", (217, 133, 108)),
    ("Tr. Green", (132, 182, 141)),
    ("Tr. Flu. Green", (248, 241, 132)),
    ("Phosph. White", (236, 232, 222)),
    ("Light red", (238, 196, 182)),
    ("Medium red", (218, 134, 122)),
    ("Medium blue", (110, 153, 202)),
    ("Light grey", (199, 193, 183)),
    ("Bright violet", (107, 50, 124)),
    ("Br. yellowish orange", (226, 155, 64)),
    ("Bright orange", (218, 133, 65)),
    ("Bright bluish green", (0, 143, 156)),
    ("Earth yellow", (104, 92, 67)),
    ("Bright bluish violet", (67, 84, 147)),
    ("Tr. Brown", (191, 183, 177)),
    ("Medium bluish violet", (104, 116, 172)),
    ("Tr. Medi. reddish violet", (229, 173, 200)),
    ("Med. yellowish green", (199, 210, 60)),
    ("Med. bluish green", (85, 165, 175)),
    ("Light bluish green", (183, 215, 213)),
    ("Br. yellowish green", (164, 189, 71)),
    ("Lig. yellowish green", (217, 228, 167)),
    ("Med. yellowish orange", (231, 172, 88)),
    ("Br. reddish orange", (211, 111, 76)),
    ("Bright reddish violet", (146, 57, 120)),
    ("Light orange", (234, 184, 146)),
    ("Tr. Bright bluish violet", (165, 165, 203)),
    ("Gold", (220, 188, 129)),
    ("Dark nougat", (174, 122, 89)),
    ("Silver", (156, 163, 168)),
    ("Neon orange", (213, 115, 61)),
    ("Neon green", (216, 221, 86)),
    ("Sand blue", (116, 134, 157)),
    ("Sand violet", (135, 124, 144)),
    ("Medium orange", (224, 152, 100)),
    ("Sand yellow", (149, 138, 115)),
    ("Earth blue", (32, 58, 86)),
    ("Earth green", (39, 70, 45)),
    ("Tr. Flu. Blue", (207, 226, 247)),
    ("Sand blue metallic", (121, 136, 161)),
    ("Sand violet metallic", (149, 142, 163)),
    ("Sand yellow metallic", (147, 135, 103)),
    ("Dark grey metallic", (87, 88, 87)),
    ("Black metallic", (22, 29, 50)),
    ("Light grey metallic", (171, 173, 172)),
    ("Sand green", (120, 144, 130)),
    ("Sand red", (149, 121, 119)),
    ("Dark red", (123, 46, 47)),
    ("Tr. Flu. Yellow", (255, 246, 123)),
    ("Tr. Flu. Red", (225, 164, 194)),
    ("Gun metallic", (117, 108, 98)),
    ("Red flip/flop", (151, 105, 91)),
    ("Yellow flip/flop", (180, 132, 85)),
    ("Silver flip/flop", (137, 135, 136)),
    ("Curry", (215, 169, 75)),
    ("Fire Yellow", (249, 214, 46)),
    ("Flame yellowish orange", (232, 171, 45)),
    ("Reddish brown", (105, 64, 40)),
    ("Flame reddish orange", (207, 96, 36)),
    ("Medium stone grey", (163, 162, 165)),
    ("Royal blue", (70, 103, 164)),
    ("Dark Royal blue", (35, 71, 139)),
    ("Bright reddish lilac", (142, 66, 133)),
    ("Dark stone grey", (99, 95, 98)),
    ("Lemon metallic", (130, 138, 93)),
    ("Light stone grey", (229, 228, 223)),
    ("Dark Curry", (176, 142, 68)),
    ("Faded green", (112, 149, 120)),
    ("Turquoise", (121, 181, 181)),
    ("Light Royal blue", (159, 195, 233)),
    ("Medium Royal blue", (108, 129, 183)),
    ("Rust", (144, 76, 42)),
    ("Brown", (124, 92, 70)),
    ("Reddish lilac", (150, 112, 159)),
    ("Lilac", (107, 98, 155)),
    ("Light lilac", (167, 169, 206)),
    ("Bright purple", (205, 98, 152)),
    ("Light purple", (228, 173, 200)),
    ("Light pink", (220, 144, 149)),
    ("Light brick yellow", (240, 213, 160)),
    ("Warm yellowish orange", (235, 184, 127)),
    ("Cool yellow", (253, 234, 141)),
    ("Dove blue", (125, 187, 221)),
    ("Medium lilac", (52, 43, 117)),
    ("Slime green", (80, 109, 84)),
    ("Smoky grey", (91, 93, 105)),
    ("Dark blue", (0, 16, 176)),
    ("Parsley green", (44, 101, 29)),
    ("Steel blue", (82, 124, 174)),
    ("Storm blue", (51, 88, 130)),
    ("Lapis", (16, 42, 220)),
    ("Dark indigo", (61, 21, 133)),
    ("Sea green", (52, 142, 64)),
    ("Shamrock", (91, 154, 76)),
    ("Fossil", (159, 161, 172)),
    ("Mulberry", (89, 34, 89)),
    ("Forest green", (31, 128, 29)),
    ("Cadet blue", (159, 173, 192)),
    ("Electric blue", (9, 137, 207)),
    ("Eggplant", (123, 0, 123)),
    ("Moss", (124, 156, 107)),
    ("Artichoke", (138, 171, 133)),
    ("Sage green", (185, 196, 177)),
    ("Ghost grey", (202, 203, 209)),
    ("Lilac", (167, 94, 155)),
    ("Plum", (123, 47, 123)),
    ("Olivine", (148, 190, 129)),
    ("Laurel green", (168, 189, 153)),
    ("Quill grey", (223, 223, 222)),
    ("Crimson", (151, 0, 0)),
    ("Mint", (177, 229, 166)),
    ("Baby blue", (152, 194, 219)),
    ("Carnation pink", (255, 152, 220)),
    ("Persimmon", (255, 89, 89)),
    ("Maroon", (117, 0, 0)),
    ("Gold", (239, 184, 56)),
    ("Daisy orange", (248, 217, 109)),
    ("Pearl", (231, 231, 236)),
    ("Fog", (199, 212, 228)),
    ("Salmon", (255, 148, 148)),
    ("Terra Cotta", (190, 104, 98)),
    ("Cocoa", (86, 36, 36)),
    ("Wheat", (241, 231, 199)),
    ("Buttermilk", (254, 243, 187)),
    ("Mauve", (224, 178, 208)),
    ("Sunrise", (212, 144, 189)),
    ("Tawny", (150, 85, 85)),
    ("Rust", (143, 76, 42)),
    ("Cashmere", (211, 190, 150)),
    ("Khaki", (226, 220, 188)),
    ("Lily white", (237, 234, 234)),
    ("Seashell", (233, 218, 218)),
    ("Burgundy", (136, 62, 62)),
    ("Cork", (188, 155, 93)),
    ("Burlap", (199, 172, 120)),
    ("Beige", (202, 191, 163)),
    ("Oyster", (187, 179, 178)),
    ("Pine Cone", (108, 88, 75)),
    ("Fawn brown", (160, 132, 79)),
    ("Hurricane grey", (149, 137, 136)),
    ("Cloudy grey", (171, 168, 158)),
    ("Linen", (175, 148, 131)),
    ("Copper", (150, 103, 102)),
    ("Dirt brown", (86, 66, 54)),
    ("Bronze", (126, 104, 63)),
    ("Flint", (105, 102, 92)),
    ("Dark taupe", (90, 76, 66)),
    ("Burnt Sienna", (106, 57, 9)),
    ("Institutional white", (248, 248, 248)),
    ("Mid gray", (205, 205, 205)),
    ("Really black", (17, 17, 17)),
    ("Really red", (255, 0, 0)),
    ("Really blue", (0, 0, 255)),
    ("Lime green", (0, 255, 0)),
    ("Hot pink", (255, 0, 191)),
]

BODY_PARTS = [
    "Head",
    "Torso",
    "LeftArm",
    "RightArm",
    "LeftLeg",
    "RightLeg"
]

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.getcwd()
    return os.path.join(base_path, relative_path)

SAVE_DIR = os.path.join("Settings", "BodyColors")
os.makedirs(SAVE_DIR, exist_ok=True)

def open_body_color_changer():
    if hasattr(open_body_color_changer, "win") and open_body_color_changer.win.winfo_exists():
        open_body_color_changer.win.lift()  # bring to front
        return

    win = ctk.CTkToplevel(root)
    open_body_color_changer.win = win  # store reference

    win.title("Avatar Editor")
    icon_path = resource_path("Logo.ico")
    if os.path.exists(icon_path):
        win.after(200, lambda: win.iconbitmap(icon_path))
    win.geometry("1100x500")
    win.resizable(False, False)

    selected_part = {"name": None}
    part_items = {}

    APPEARANCE_FILE = os.path.join("Settings", "Appearence.ini")
    os.makedirs("Settings", exist_ok=True)

    # ---------------- Helper functions ----------------
    def rgb_to_hex(rgb):
        return "#%02x%02x%02x" % rgb

    def save_color(part, color_name):
        os.makedirs(SAVE_DIR, exist_ok=True)
        with open(os.path.join(SAVE_DIR, f"{part}Color.txt"), "w", encoding="utf-8") as f:
            f.write(color_name)

    def read_color(part):
        path = os.path.join(SAVE_DIR, f"{part}Color.txt")
        if os.path.exists(path):
            name = open(path, "r").read().strip()
            for cname, rgb in ROBLOX_COLORS:
                if cname == name:
                    return rgb
        return (150, 150, 150)

    def select_part(part):
        selected_part["name"] = part
        for item in part_items.values():
            canvas.itemconfig(item, width=1)
        canvas.itemconfig(part_items[part], width=3)

    def apply_color(color_name, rgb):
        if not selected_part["name"]:
            return
        canvas.itemconfig(part_items[selected_part["name"]], fill=rgb_to_hex(rgb))
        save_color(selected_part["name"], color_name)

    # ---------------- Appearance functions ----------------
    def load_appearance():
        if not os.path.exists(APPEARANCE_FILE):
            with open(APPEARANCE_FILE, "w") as f:
                f.write("http://localhost/charscript/Custom.php?hat=0\n")
        with open(APPEARANCE_FILE, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
        if not lines or not lines[0].startswith("http://localhost/charscript/Custom.php?hat=0"):
            lines.insert(0, "http://localhost/charscript/Custom.php?hat=0")
        return lines

    def save_appearance(lines):
        with open(APPEARANCE_FILE, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
        refresh_list()

    # ---------------- Layout Frames ----------------
    # Left: Humanoid Canvas
    left_frame = ctk.CTkFrame(win, corner_radius=10)
    left_frame.pack(side="left", padx=10, pady=10)

    canvas = ctk.CTkCanvas(left_frame, width=300, height=310, bg="#2b2b2b")
    canvas.pack()

    # R6 proportions
    TORSO_WIDTH, TORSO_HEIGHT = 100, 100
    ARM_WIDTH, LEG_WIDTH = 50, 50
    HEAD_WIDTH, HEAD_HEIGHT = 60, 60
    torso_x, torso_y = 100, 80
    leg_y_start = torso_y + TORSO_HEIGHT
    leg_height = 120

    part_items["Torso"] = canvas.create_rectangle(
        torso_x, torso_y, torso_x + TORSO_WIDTH, torso_y + TORSO_HEIGHT,
        fill=rgb_to_hex(read_color("Torso"))
    )
    part_items["Head"] = canvas.create_rectangle(
        torso_x + (TORSO_WIDTH - HEAD_WIDTH)//2, torso_y - HEAD_HEIGHT,
        torso_x + (TORSO_WIDTH - HEAD_WIDTH)//2 + HEAD_WIDTH, torso_y,
        fill=rgb_to_hex(read_color("Head"))
    )
    part_items["RightArm"] = canvas.create_rectangle(
        torso_x - ARM_WIDTH, torso_y, torso_x, torso_y + TORSO_HEIGHT,
        fill=rgb_to_hex(read_color("RightArm"))
    )
    part_items["LeftArm"] = canvas.create_rectangle(
        torso_x + TORSO_WIDTH, torso_y, torso_x + TORSO_WIDTH + ARM_WIDTH, torso_y + TORSO_HEIGHT,
        fill=rgb_to_hex(read_color("LeftArm"))
    )
    part_items["LeftLeg"] = canvas.create_rectangle(
        torso_x, leg_y_start, torso_x + LEG_WIDTH, leg_y_start + leg_height,
        fill=rgb_to_hex(read_color("LeftLeg"))
    )
    part_items["RightLeg"] = canvas.create_rectangle(
        torso_x + 50, leg_y_start, torso_x + 50 + LEG_WIDTH, leg_y_start + leg_height,
        fill=rgb_to_hex(read_color("RightLeg"))
    )

    for part, item in part_items.items():
        canvas.tag_bind(item, "<Button-1>", lambda e, p=part: select_part(p))

    # Center: Color Palette
    center_frame = ctk.CTkScrollableFrame(win, width=200, corner_radius=10)
    center_frame.pack(side="left", padx=5, pady=10, fill="both", expand=True)

    ctk.CTkLabel(center_frame, text="Click a color to apply to selected part:").pack(pady=5)
    for name, rgb in ROBLOX_COLORS:
        btn = ctk.CTkButton(center_frame, text=name, fg_color=rgb_to_hex(rgb), hover_color=rgb_to_hex(rgb),
                            command=lambda n=name, r=rgb: apply_color(n, r))
        btn.pack(fill="x", pady=2, padx=5)

    # Right: Avatar Item Inserter
    right_frame = ctk.CTkFrame(win, corner_radius=10)
    right_frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    ctk.CTkLabel(right_frame, text="Avatar Item Inserter").pack(pady=5)

    # Entry + buttons
    asset_entry = ctk.CTkEntry(right_frame)
    asset_entry.pack(pady=(0,5), fill="x", padx=5)

    def add_asset():
        assetid = asset_entry.get().strip()
        if not assetid.isdigit():
            return
        lines = load_appearance()
        lines.append(f";http://localhost/asset/?id=1111111{assetid}")
        save_appearance(lines)
        asset_entry.delete(0, "end")

    def reset_appearance():
        save_appearance(["http://localhost/charscript/Custom.php?hat=0"])

    btn_frame = ctk.CTkFrame(right_frame)
    btn_frame.pack(fill="x", pady=5)
    ctk.CTkButton(btn_frame, text="Add", command=add_asset).pack(side="left", expand=True, padx=2)
    ctk.CTkButton(btn_frame, text="Reset", command=reset_appearance).pack(side="left", expand=True, padx=2)

    # Listbox replacement using CTkScrollableFrame
    listbox_frame = ctk.CTkScrollableFrame(right_frame, height=250)
    listbox_frame.pack(fill="both", expand=True, pady=5)

    list_items = []

    def refresh_list():
        # Clear
        for w in listbox_frame.winfo_children():
            w.destroy()
        lines = load_appearance()[1:]  # skip first line
        list_items.clear()
        for line in lines:
            display = line.replace(";http://localhost/asset/?id=1111111", "") if line.startswith(";http://localhost/asset/?id=1111111") else line
            lbl = ctk.CTkLabel(listbox_frame, text=display, anchor="w")
            lbl.pack(fill="x", pady=1, padx=3)
            lbl.bind("<Double-1>", lambda e, l=line: remove_item(l))

            list_items.append(lbl)

    def remove_item(line_to_remove):
        lines = load_appearance()
        lines = [l for l in lines if l != line_to_remove]
        save_appearance(lines)
        refresh_list()

    refresh_list()

def load_body_type():
    path = os.path.join("Settings", "BodyType.txt")
    if os.path.exists(path):
        return open(path, "r").read().strip()
    return "R6"

def load_FE_type():
    path = os.path.join("Settings", "FilteringToggle.txt")
    if os.path.exists(path):
        return open(path, "r").read().strip()
    return "true"

def load_AS_type():
    path = os.path.join("Settings", "assetsaving", "Enabled.txt")
    if os.path.exists(path):
        return open(path, "r").read().strip()
    return "true"

def save_AS_type(value):
    os.makedirs("Settings", exist_ok=True)
    with open(os.path.join("Settings", "assetsaving", "Enabled.txt"), "w") as f:
        f.write(value)

def save_FE_type(value):
    os.makedirs("Settings", exist_ok=True)
    with open(os.path.join("Settings", "FilteringToggle.txt"), "w") as f:
        f.write(value)

def save_body_type(value):
    os.makedirs("Settings", exist_ok=True)
    with open(os.path.join("Settings", "BodyType.txt"), "w") as f:
        f.write(value)

def edit_map():
    try:
        base = os.getcwd()

        map_path_file = os.path.join(base, "Settings", "MapPath.txt")
        if not os.path.exists(map_path_file):
            return

        map_path = open(map_path_file, "r").read().strip()
        if not os.path.exists(map_path):
            return

        copy_targets = [
            "Webserver/www/.127.0.0.1/asset/1818",
            "Webserver/www/.localhost/asset/1818",
            "shared/content/place.rbxl",
            "shared/content/1818",
            "Clients/2014M/content/temp.rbxl"
        ]

        for rel in copy_targets:
            dest = os.path.join(base, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            if os.path.exists(dest):
                os.remove(dest)
            shutil.copy(map_path, dest)

        # Fix.ini
        fix_ini = open(os.path.join(base, "Settings", "Fix.ini")).read()

        server_xml = f"""<roblox xmlns:xmime={fix_ini}http://www.w3.org/2005/05/xmlmime{fix_ini}
xmlns:xsi={fix_ini}http://www.w3.org/2001/XMLSchema-instance{fix_ini}
xsi:noNamespaceSchemaLocation={fix_ini}http://www.localhost//roblox.xsd{fix_ini}
version={fix_ini}4{fix_ini}>
<External>null</External>
<External>nil</External>
<Item class={fix_ini}Script{fix_ini}>
<Properties>
<bool name={fix_ini}Disabled{fix_ini}>false</bool>
<string name={fix_ini}Name{fix_ini}>Script</string>
<ProtectedString name={fix_ini}Source{fix_ini}><![CDATA[_G.FilteringEnabled=true]]></ProtectedString>
</Properties>
</Item>
</roblox>"""

        server_path = os.path.join(base, "shared", "content", "server.rbxmx")
        with open(server_path, "w") as f:
            f.write(server_xml)

        # create EditMap.bat
        studio = os.path.join(base, "Clients", "2022M", "RobloxStudioBeta.exe")
        bat_path = os.path.join(base, "Settings", "EditMap.bat")

        with open(bat_path, "w") as f:
            f.write(f'"{studio}" -localPlaceFile "{map_path}"\nexit')

        subprocess.Popen(["cmd", "/c", "start", bat_path], shell=True)

    except Exception as e:
        print("EditMap error:", e)

def read_body_colors():
    base = os.path.join("Settings", "BodyColors")

    files = [
        "HeadColor.txt",
        "TorsoColor.txt",
        "LeftArmColor.txt",
        "RightArmColor.txt",
        "LeftLegColor.txt",
        "RightLegColor.txt",
    ]

    colors = []

    for file in files:
        path = os.path.join(base, file)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                colors.append(f.read().strip())
        else:
            colors.append("0")  # fallback

    return ";".join(colors)

def read_appearance():
    path = os.path.join("Settings", "Appearence.ini")

    if not os.path.exists(path):
        return ""

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        data = f.read()

    # remove ALL whitespace and replace with ;
    data = re.sub(r"\s+", ";", data)
    return data

def build_app_arg():
    appearance = read_appearance()
    body_colors = read_body_colors()
    return f"{appearance}|{body_colors}"

def save_setting(file_name, value):
    path = os.path.join(SETTINGS_DIR, file_name)
    os.makedirs(SETTINGS_DIR, exist_ok=True)
    with open(path, "w") as f:
        f.write(str(value))

def read_setting(file_name, default=""):
    path = os.path.join(SETTINGS_DIR, file_name)
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read().strip()
    return default

def random_id():
    return random.randint(10000, 99999)

def find_client_executable(client_version):
    client_folder = os.path.join(CLIENTS_DIR, client_version)

    # 1. Any EXE in client folder
    exe_files = glob.glob(os.path.join(client_folder, "*.exe"))
    if exe_files:
        return exe_files[0]

    # 2. Player subfolder
    player_folder = os.path.join(client_folder, "Player")
    if os.path.exists(player_folder):
        exe_files = glob.glob(os.path.join(player_folder, "*.exe"))
        if exe_files:
            return exe_files[0]

    # 3. RCCService folder
    rcc_folder = os.path.join(client_folder, "RCCService")
    if os.path.exists(rcc_folder):
        exe_files = glob.glob(os.path.join(rcc_folder, "*.exe"))
        if exe_files:
            return exe_files[0]

    # 4. Player folder fallback
    if os.path.exists(player_folder):
        exe_files = glob.glob(os.path.join(player_folder, "RCCService.exe"))
        if exe_files:
            return exe_files[0]
        exe_files = glob.glob(os.path.join(player_folder, f"{client_version}.exe"))
        if exe_files:
            return exe_files[0]

    # 5. Fallback to .bat in client folder
    bat_files = glob.glob(os.path.join(client_folder, "*.bat"))
    if bat_files:
        return bat_files[0]

    return None

# Server process handle
server_proc = None

def copy_map(file_path):
    if not os.path.exists(file_path):
        return
    paths = [
        os.path.join(BASE_DIR, "Webserver/www/.127.0.0.1/asset/1818"),
        os.path.join(BASE_DIR, "Webserver/www/.localhost/asset/1818"),
        os.path.join(SHARED_DIR, "content/place.rbxl"),
        os.path.join(SHARED_DIR, "content/1818"),
        os.path.join(CLIENTS_DIR, "2014M/content/temp.rbxl"),
    ]
    for dest in paths:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        if os.path.exists(dest):
            os.remove(dest)
        try:
            shutil.copy(file_path, dest)
        except Exception as e:
            print(e)
    save_setting("MapPath.txt", file_path)

def select_map():
    file_path = filedialog.askopenfilename(title="Select Roblox Map", filetypes=[("Roblox files", "*.rbxl")])
    if file_path:
        copy_map(file_path)

def launch_server(client_version):
    global server_proc
    server_bat = os.path.join(SHARED_DIR, f"{client_version}.bat")
    if os.path.exists(server_bat):
        server_proc = subprocess.Popen(f'start cmd /k "{server_bat}"', shell=True)
    else:
        messagebox.showwarning("Warning", f"No server bat found for {client_version}")

def launch_client(client_version):
    client_exec = find_client_executable(client_version)
    if not client_exec and client_version == "2015L":
        client_exec = os.path.join(".", "shared", "2015Player.exe")
    
    if not client_exec:
        messagebox.showerror("Error", f"Could not find executable or bat for client {client_version}")
        return
    
    # Launch the client normally
    try:
        subprocess.Popen([client_exec])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch client: {e}")

    username = username_var.get() or "Player"
    ip = ip_var.get() or "localhost"
    port = port_var.get() or "2005"
    session_id = random_id()

    app_data = build_app_arg()
    quote = '"'

    # ---- BAT fallback ----
    if client_exec.lower().endswith(".bat"):
        subprocess.Popen([client_exec], shell=True)
        return

    # ---- VERSION-SPECIFIC LOGIC ----
    if client_version in ("2015L", "2016L"):
        join = (
            f"http://{ip}/game/placelaunchrrr.php/?"
            f"placeid=1818&ip={ip}&port={port}&id={session_id}"
            f"&app={app_data}&user={username}"
        )
        auth = f"http://{ip}/login/negotiate.ashx"

    elif client_version == "2017M":
        join = (
            f"http://{ip}/game/join.php/?"
            f"placeid=1818&ip={ip}&port={port}&id={session_id}"
            f"&app={app_data}&user={username}"
        )
        auth = f"http://{ip}/login/negotiate.ashx"

    elif client_version in ("2020L", "2021E"):
        app_data = app_data.replace("1111111", "")
        join = (
            f"http://{ip}/2021/game/placelauncher.ashx?"
            f"placeid=1818&ip={ip}&user={username}"
            f"&port={port}&id={session_id}&app={app_data}"
        )
        auth = f"http://{ip}/2021/login/negotiate.ashx"

    elif client_version.startswith("2019"):
        join = (
            f"http://{ip}/game/placelauncher.ashx?"
            f"placeid=1818&ip={ip}&port={port}"
            f"&id={session_id}&app={app_data}&user={username}"
        )
        auth = f"http://{ip}/login/negotiate.ashx"

    else:
        # ---- GENERIC FALLBACK ----
        app_data = app_data.replace("1111111", "")
        join = (
            f"http://{ip}/game/placelauncher.ashx?"
            f"year=2018&placeid=1818&ip={ip}&port={port}"
            f"&id={session_id}&app={app_data}&user={username}"
        )
        auth = f"http://{ip}/login/negotiate.ashx"

    # ---- FINAL COMMAND ----
    cmd = (
        f'{quote}{client_exec}{quote} '
        f'-a {quote}{auth}{quote} '
        f'-j {quote}{join}{quote} '
        f'-t {quote}1{quote}'
    )

    subprocess.Popen(cmd, shell=True)

# ---- GUI ----
ctk.set_appearance_mode("Dark")  # "Dark" or "Light"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

# --- Root window ---
root = ctk.CTk()
root.title("RetroStud")
icon_path = resource_path("Logo.ico")
root.iconbitmap(icon_path)
root.geometry("360x750")
root.resizable(False, False)

# --- Frames ---
top_frame = ctk.CTkFrame(root, corner_radius=10)
top_frame.pack(padx=10, pady=10, fill="x")

config_frame = ctk.CTkFrame(root, corner_radius=10)
config_frame.pack(padx=10, pady=5, fill="x")

actions_frame = ctk.CTkFrame(root, corner_radius=10)
actions_frame.pack(padx=10, pady=10, fill="x")

# --- Client Version ---
ctk.CTkLabel(top_frame, text="Client:", anchor="w").pack(fill="x", pady=(5,2))
client_var = ctk.StringVar()
clients = [d for d in os.listdir(CLIENTS_DIR) if os.path.isdir(os.path.join(CLIENTS_DIR, d))]
client_dropdown = ctk.CTkComboBox(top_frame, variable=client_var, values=clients)
client_dropdown.pack(fill="x", pady=(0,5))

# --- Configuration ---
ctk.CTkLabel(config_frame, text="Configuration:", anchor="w").pack(fill="x", pady=(5,2))

ctk.CTkLabel(config_frame, text="IP:", anchor="w").pack(fill="x", pady=(5,0))
ip_var = ctk.StringVar(value=read_setting("ip.txt", "localhost"))
ctk.CTkEntry(config_frame, textvariable=ip_var).pack(fill="x", pady=(0,2))

ctk.CTkLabel(config_frame, text="Port:", anchor="w").pack(fill="x", pady=(5,0))
port_var = ctk.StringVar(value=read_setting("clientport.txt", "2005"))
ctk.CTkEntry(config_frame, textvariable=port_var).pack(fill="x", pady=(0,2))

ctk.CTkLabel(config_frame, text="Username:", anchor="w").pack(fill="x", pady=(5,0))
username_var = ctk.StringVar(value=read_setting("username.txt", "Player"))
ctk.CTkEntry(config_frame, textvariable=username_var).pack(fill="x", pady=(0,2))

FE_var = ctk.StringVar(value=load_FE_type())
AS_var = ctk.StringVar(value=load_AS_type())

def on_FE_change(*args):
    os.makedirs("Settings", exist_ok=True)
    save_FE_type(FE_var.get())

def on_AS_change(*args):
    os.makedirs(os.path.join("Settings", "assetsaving"), exist_ok=True)
    save_AS_type(AS_var.get())

# Trace changes instead of bind
FE_var.trace_add("write", on_FE_change)
AS_var.trace_add("write", on_AS_change)

ctk.CTkLabel(config_frame, text="Filtering Enabled:", anchor="w").pack(fill="x", pady=(5,0))
FE_type_dropdown = ctk.CTkComboBox(config_frame, variable=FE_var, values=["true", "false"])
FE_type_dropdown.pack(fill="x", pady=(0,5))

ctk.CTkLabel(config_frame, text="Asset Saving:", anchor="w").pack(fill="x", pady=(5,0))
AS_type_dropdown = ctk.CTkComboBox(config_frame, variable=AS_var, values=["true", "false"])
AS_type_dropdown.pack(fill="x", pady=(0,5))

# --- Body Type ---
body_type_var = ctk.StringVar(value=load_body_type())
def on_body_type_change(event=None):
    save_body_type(body_type_var.get())

ctk.CTkLabel(config_frame, text="Body Type:", anchor="w").pack(fill="x", pady=(5,0))
body_type_dropdown = ctk.CTkComboBox(config_frame, variable=body_type_var, values=["R6", "R15"])
body_type_dropdown.pack(fill="x", pady=(0,5))
body_type_dropdown.bind("<<ComboboxSelected>>", on_body_type_change)

# --- Map & Avatar buttons ---
ctk.CTkButton(config_frame, text="Select Map", command=select_map).pack(fill="x", pady=(3,3))
ctk.CTkButton(config_frame, text="Edit Map", command=edit_map).pack(fill="x", pady=(3,3))
ctk.CTkButton(config_frame, text="Avatar Editor", command=open_body_color_changer).pack(fill="x", pady=(3,5))

# --- Actions ---
ctk.CTkLabel(actions_frame, text="Actions:", anchor="w").pack(fill="x", pady=(5,2))
ctk.CTkButton(actions_frame, text="Launch Server", command=lambda: launch_server(client_var.get())).pack(fill="x", pady=3)
ctk.CTkButton(actions_frame, text="Launch Client", command=lambda: launch_client(client_var.get())).pack(fill="x", pady=3)

root.mainloop()
