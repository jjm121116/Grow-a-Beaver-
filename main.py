# =========================
# BEAVER DATA
# =========================

BEAVERS = [
    "Tiny Beaver", "Wood Beaver", "River Beaver", "Stone Beaver", "Forest Beaver",
    "Iron Beaver", "Golden Beaver", "Royal Beaver", "Battle Beaver", "Crystal Beaver",
    "Shadow Beaver", "Lava Beaver", "Storm Beaver", "Frozen Beaver", "Mythic Beaver",
    "Dragon Beaver", "Galaxy Beaver", "Cyber Beaver", "Project Hailmary Beaver", "Noob(?) Beaver",
    "Nightmare Beaver", "Void Beaver", "Ancient Beaver", "Quantum Beaver", "Martial law Beaver",
    "Inferno Beaver", "Celestial Beaver", "Toxic Beaver", "Chrono Beaver", "Owlrock Beaver",
    "Dimension Beaver", "Aura Beaver", "Dark Star Beaver", "Blood Moon Beaver", "Drinking Beaver",
    "God Beaver", "Nita Beaver", "Blue Beaver", "Glitch Beaver", "Rainbow Beaver",
    "Heaven Beaver", "Hell Beaver", "Invisible Beaver", "Hell's ultimate guard", "Beaver^33",
    "Red Beaver", "Black Hole Beaver", "King Beaver", "Final Beaver", "Synchronized Beaver", "TRUE BEAVER"
]

BASE_RATES = [
    100,95,90,85,80,76,72,68,64,60,
    57,54,51,48,45,42,39,36,33,30,
    28,26,24,22,20,18,16,14,12,10,
    9,8.5,8,7.5,7,6.5,6,5.5,5,4.5,
    4,3.8,3.6,3.4,3.2,3,2.8,2.6,2.4,2.2
]

# =========================
# GAME CLASS
# =========================

class BeaverGame:

    def __init__(self, root):

        self.root = root
        self.root.title("🦫 Beaver Growing Game")
        self.root.geometry("800x800")
        self.root.configure(bg="#1b1b1b")

        # GAME VARIABLES
        self.level = 0
        self.money = 1000
        self.protection = 1
        self.skip_ticket = 1
        self.hardmode = 0
        self.prev_beavers = 0

        self.fail_streak = 0

        # =========================
        # UI
        # =========================

        self.title = tk.Label(
            root,
            text="🦫 BEAVER GROWING GAME",
            font=("Arial", 28, "bold"),
            fg="white",
            bg="#1b1b1b"
        )
        self.title.pack(pady=10)

        # BEAVER IMAGE
        self.image_label = tk.Label(
            root,
            bg="#1b1b1b"
        )
        self.image_label.pack(pady=10)

        self.beaver_label = tk.Label(
            root,
            text="Tiny Beaver",
            font=("Arial", 22, "bold"),
            fg="orange",
            bg="#1b1b1b"
        )
        self.beaver_label.pack()

        self.level_label = tk.Label(
            root,
            text="Level: 0",
            font=("Arial", 16),
            fg="white",
            bg="#1b1b1b"
        )
        self.level_label.pack()

        self.rate_label = tk.Label(
            root,
            text="Upgrade Rate: 100%",
            font=("Arial", 16),
            fg="lightgreen",
            bg="#1b1b1b"
        )
        self.rate_label.pack()

        self.money_label = tk.Label(
            root,
            text="Money: 1000",
            font=("Arial", 16),
            fg="gold",
            bg="#1b1b1b"
        )
        self.money_label.pack(pady=5)

        self.inventory_label = tk.Label(
            root,
            text="Protection: 0 | Skip Tickets: 0",
            font=("Arial", 14),
            fg="white",
            bg="#1b1b1b"
        )
        self.inventory_label.pack()

        self.fail_label = tk.Label(
            root,
            text="Fail Streak: 0 / 3",
            font=("Arial", 14),
            fg="red",
            bg="#1b1b1b"
        )
        self.fail_label.pack(pady=5)

        # =========================
        # BUTTONS
        # =========================

        self.upgrade_btn = tk.Button(
            root,
            text="UPGRADE",
            font=("Arial", 20, "bold"),
            width=20,
            height=2,
            bg="#4CAF50",
            fg="white",
            command=self.upgrade
        )
        self.upgrade_btn.pack(pady=15)

        self.shop_frame = tk.Frame(root, bg="#1b1b1b")
        self.shop_frame.pack()

        self.buy_protect_btn = tk.Button(
            self.shop_frame,
            text="Buy Protection (300)",
            width=20,
            command=self.buy_protection
        )
        self.buy_protect_btn.grid(row=0, column=0, padx=10)

        self.buy_skip_btn = tk.Button(
            self.shop_frame,
            text="Buy Skip Ticket (500)",
            width=20,
            command=self.buy_skip
        )
        self.buy_skip_btn.grid(row=0, column=1, padx=10)

        self.skip_btn = tk.Button(
            root,
            text="USE SKIP TICKET (50%)",
            width=30,
            height=2,
            command=self.use_skip
        )
        self.skip_btn.pack(pady=15)

        # LOG
        self.log = tk.Text(
            root,
            height=10,
            bg="black",
            fg="lime",
            font=("Consolas", 11)
        )
        self.log.pack(fill="x", padx=10, pady=10)

        self.update_ui()

    # =========================
    # IMAGE SYSTEM
    # =========================

    def load_beaver_image(self):

        path = f"beavers/{self.level}.png"

        if os.path.exists(path):

            img = Image.open(path)

        else:
            # Placeholder image if missing
            img = Image.new("RGB", (250, 250), color="gray")

        img = img.resize((250, 250))

        self.tk_img = ImageTk.PhotoImage(img)

        self.image_label.config(image=self.tk_img)

    # =========================
    # RATE
    # =========================

    def get_rate(self):

        if self.level >= 50:
            return 1

        rate = BASE_RATES[self.level]

        rate -= self.hardmode * 5

        if rate < 1:
            rate = 1

        return rate

    # =========================
    # UPDATE UI
    # =========================

    def update_ui(self):

        self.beaver_label.config(
            text=BEAVERS[self.level]
        )

        self.level_label.config(
            text=f"Level: {self.level}"
        )

        self.rate_label.config(
            text=f"Upgrade Rate: {self.get_rate()}%"
        )

        self.money_label.config(
            text=f"Money: {self.money}"
        )

        self.inventory_label.config(
            text=f"Protection: {self.protection} | Skip Tickets: {self.skip_ticket}"
        )

        self.fail_label.config(
            text=f"Fail Streak: {self.fail_streak} / 3"
        )

        self.load_beaver_image()

    # =========================
    # LOG
    # =========================

    def log_message(self, msg):

        self.log.insert(tk.END, msg + "\n")
        self.log.see(tk.END)

    # =========================
    # SHOP
    # =========================

    def buy_protection(self):

        if self.money >= 300:

            self.money -= 300
            self.protection += 1

            self.log_message("Bought Protection!")

        else:

            self.log_message("Not enough money!")

        self.update_ui()

    def buy_skip(self):

        if self.money >= 500:

            self.money -= 500
            self.skip_ticket += 1

            self.log_message("Bought Skip Ticket!")

        else:

            self.log_message("Not enough money!")

        self.update_ui()

    # =========================
    # SKIP TICKET
    # =========================

    def use_skip(self):

        if self.skip_ticket <= 0:

            self.log_message("No Skip Tickets!")
            return

        if self.level >= 49:

            self.log_message("MAX LEVEL!")
            return

        self.skip_ticket -= 1

        roll = random.randint(1, 100)

        # 50% SUCCESS
        if roll <= 50:

            self.level += 1
            self.fail_streak = 0

            self.log_message("SKIP SUCCESS!")

        else:

            self.fail_streak += 1

            self.log_message("SKIP FAILED!")

            self.check_fail_reset()

        self.check_hardmode()
        self.update_ui()

    # =========================
    # FAIL RESET SYSTEM
    # =========================

    def check_fail_reset(self):
        if self.protection == 0 : 
            if self.fail_streak >= 3:

                self.money -= 200*self.level
                self.level = 1
                self.fail_streak = 0

                self.log_message("💀 3 FAILS IN A ROW!")
                self.log_message("Beaver reset to LEVEL 1!")
                self.log_message("A robber beaver has stolen money from you! ")

                messagebox.showwarning(
                    "RESET",
                    "3 FAILS IN A ROW!\n\nYour Beaver reset to Lv1!"
                )

    # =========================
    # UPGRADE
    # =========================

    def upgrade(self):

        if self.level >= 49:

            self.log_message("MAX LEVEL!")
            return

        # Lv30+ requirement
        if self.level >= 30:

            if self.prev_beavers <= 0:

                self.log_message("Need 1 Previous Beaver!")
                return

            else:

                self.prev_beavers -= 1

        rate = self.get_rate()

        roll = random.uniform(0, 100)

        if roll <= rate:

            self.level += 1

            reward = 100 + self.level * 25

            self.money += reward

            self.fail_streak = 0

            self.log_message(
                f"SUCCESS -> {BEAVERS[self.level]}"
            )

            self.log_message(
                f"+{reward} money"
            )

            if self.level >= 30:
                self.prev_beavers += 1

        else:

            self.fail_streak += 1

            # Protection
            if self.protection > 0:

                self.protection -= 1

                self.log_message(
                    "FAILED! Protection saved your beaver!"
                )

            else:

                self.log_message("FAILED!")

                if self.level > 0:
                    self.level -= 1

            self.check_fail_reset()

        self.check_hardmode()
        self.update_ui()

    # =========================
    # HARDMODE
    # =========================

    def check_hardmode(self):

        if self.level >= 50:

            self.hardmode += 1

            messagebox.showinfo(
                "HARD MODE",
                f"HARD MODE {self.hardmode} START!\n\nUpgrade rates decreased by 5%!"
            )

            self.level = 0
            self.prev_beavers = 0

            self.log_message(
                f"=== HARD MODE {self.hardmode} STARTED ==="
            )

# =========================
# START GAME
# =========================

root = tk.Tk()

game = BeaverGame(root)

root.mainloop()
