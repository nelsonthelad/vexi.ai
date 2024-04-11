import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI

client = OpenAI(api_key="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")

def createView():
    app = tk.Tk()
    app.title("")
    app.geometry("600x800")

    frame = tk.Frame(app, bd=2, relief=tk.SOLID, bg="black")
    frame.pack(padx=0, pady=0, fill=tk.X)
    header = tk.Label(frame, text="vexi.ai", font=("Ke$ha", 32, "bold"), fg="white", bg="black")
    header.pack(padx=10, pady=10)

    subFrame = tk.Frame(app, bd=2, relief=tk.SOLID, bg="grey")
    subFrame.pack(padx=0, pady=0, fill=tk.X)

    input = tk.Entry(app, width=500)
    input.pack(side=tk.BOTTOM, padx=10, pady=10)
    input.bind("<Return>", lambda event: processUserInput(input, output))

    output = scrolledtext.ScrolledText(app, width=500, height=600, state="disabled")
    output.pack()

    app.mainloop()

def processUserInput(input_text, output):
    user_input = input_text.get()
    if user_input:
        input_text.delete(0, tk.END) 
        output.config(state="normal")  
        output.insert(tk.END, f"User: {user_input}\n")

        chatgpt_response = get_ai_response(user_input)
        output.insert(tk.END, f"Vexi: {chatgpt_response}\n")
        output.config(state="disabled") 

def get_ai_response(input):
    if input:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": input,
                }
            ],
            model="gpt-3.5-turbo-0125",
        )
        message_content = response.choices[0].message.content
    
    return message_content

def main():
    createView()

main()
