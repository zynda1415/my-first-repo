import random
import time

class FunnyBot:
    def __init__(self, name="🤖 FunnyBot", log_file="jokes.log"):
        self.name = name
        self.log_file = log_file
        self.jokes = [
            "Why don’t scientists trust atoms? Because they make up everything! 😂",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
            "I told my computer I needed a break, and it said “No problem – I’ll go to sleep.” 😴",
            "Why do Python programmers wear glasses? Because they can’t C! 🐍👓"
        ]

    def tell_joke(self):
        joke = random.choice(self.jokes)
        line = f"{self.name} says: {joke}"
        print(line)
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(line + "\n")

    def run(self):
        print("\n" + "="*30)
        print(f" START of {self.name} output ")
        print("="*30 + "\n")

        # decide how many jokes (non‑interactive fallback)
        try:
            n = int(input("How many jokes? "))
        except:
            n = 2

        # clear old log
        open(self.log_file, "w").close()

        for i in range(n):
            self.tell_joke()
            time.sleep(0.5)

        print("\n" + "-"*30)
        print("Log of jokes:")
        print("-"*30)
        # show the log file
        for line in open(self.log_file, encoding="utf-8"):
            print(line.strip())

        print("\n=== END ===")

if __name__ == "__main__":
    bot = FunnyBot()
    bot.run()
