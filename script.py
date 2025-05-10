import random
import time
import os

class FunnyBot:
    def __init__(self, name="🤖 FunnyBot"):
        self.name = name
        self.jokes = [
            "Why don’t scientists trust atoms? Because they make up everything! 😂",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
            "I told my computer I needed a break, and it said “No problem – I’ll go to sleep.” 😴",
            "Why do Python programmers wear glasses? Because they can’t C! 🐍👓"
        ]
        # simple ASCII‑dance frames
        self.dance_moves = [
            r"(•_•) ♪", r"( •_•)>⌐■-■ ♪", r"(⌐■_■) ♪", r"\(^_^)/ ♪", r"(╯°□°）╯︵ ┻━┻ ♪"
        ]

    def clear_screen(self):
        """Clear console (Windows ‘cls’, others ‘clear’)."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def tell_joke(self):
        joke = random.choice(self.jokes)
        print(f"\n{self.name} says: {joke}")

    def ascii_dance(self, steps=5, delay=0.3):
        print("\nTime to dance! 💃🕺")
        for i in range(steps):
            frame = random.choice(self.dance_moves)
            print(frame, end="\r", flush=True)
            time.sleep(delay)
        print()  # newline after dance

    def run(self):
        self.clear_screen()
        print(f"Welcome to {self.name}!\n")
        time.sleep(1)

        # Ask user how many jokes
           try:
          n = int(input("How many jokes would you like? "))
      except ValueError:
          n = 1
      try:
         # interactive prompt; if it fails, default to 1
          n = int(input("How many jokes would you like? "))
      except (ValueError, EOFError):
           n = 1


        for i in range(n):
            self.tell_joke()
            time.sleep(1)
            self.ascii_dance(steps=3)

        print("\nThat's all folks! 🎉")

if __name__ == "__main__":
    bot = FunnyBot()
    bot.run()
