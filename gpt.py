import tkinter as tk
from tkinter import scrolledtext, messagebox
import openai

# Set your OpenAI API key here
api_key = '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'

# Initialize the OpenAI GPT API client
openai.api_key = api_key

def ask_question():
    question = user_input.get("1.0", tk.END).strip()
    if question:
        chat_log.configure(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + question + "\n")
        chat_log.configure(state=tk.DISABLED)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=100
        )

        bot_reply = response['choices'][0]['message']['content']
        chat_log.configure(state=tk.NORMAL)
        chat_log.insert(tk.END, "Bot: " + bot_reply + "\n")
        chat_log.configure(state=tk.DISABLED)
        user_input.delete("1.0", tk.END)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Simple Chatbot")

chat_frame = tk.Frame(root)
chat_frame.pack(pady=10)

chat_log = scrolledtext.ScrolledText(chat_frame, width=50, height=20)
chat_log.configure(state=tk.DISABLED)
chat_log.pack()

user_input = tk.Text(root, width=40, height=3)
user_input.pack(pady=10)

send_button = tk.Button(root, text="Send", command=ask_question)
send_button.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
