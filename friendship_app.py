import tkinter as tk
from tkinter import messagebox

def generate_badge():
    name = name_entry.get()
    trait = trait_entry.get()
    emoji = emoji_entry.get()

    if name and trait and emoji:
        badge = f"""
        🎉 Happy Friendship Day, {name.title()}! 🎉

        You're truly {trait}! Never change! {emoji}

        From your forever friend ❤️ Atharva
        """
        messagebox.showinfo("Your Friendship Badge", badge)
    else:
        messagebox.showwarning("Oops!", "Please fill in all the fields!")

# GUI 
root = tk.Tk()
root.title("Friendship Badge Generator")
root.geometry("400x300")
root.config(bg="#fff0f5")

title = tk.Label(root, text="💖 Friendship Badge Generator 💖", font=("Arial", 16), bg="#fff0f5", fg="#ff1493")
title.pack(pady=10)

tk.Label(root, text="Friend's Name:", bg="#fff0f5").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="What you love about them:", bg="#fff0f5").pack()
trait_entry = tk.Entry(root)
trait_entry.pack()

tk.Label(root, text="An emoji that reminds you of them:", bg="#fff0f5").pack()
emoji_entry = tk.Entry(root)
emoji_entry.pack()

tk.Button(root, text="Generate Badge 🎁", command=generate_badge, bg="#ff69b4", fg="white").pack(pady=15)

root.mainloop()
