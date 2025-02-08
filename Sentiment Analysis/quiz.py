import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

nltk.download('vader_lexicon')

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    words = text.split()
    word_scores = {word: sia.polarity_scores(word)['compound'] for word in words}
    
    if score['compound'] >= 0.05:
        sentiment = 'Positive 😊'
        color = '#2ecc71'
    elif score['compound'] <= -0.05:
        sentiment = 'Negative 😠'
        color = '#e74c3c'
    else:
        sentiment = 'Neutral 😐'
        color = '#3498db'
    
    return sentiment, score, word_scores, color

def create_table(frame, data):
    tree = ttk.Treeview(frame, columns=('Word', 'Score'), show='headings', height=5)
    tree.column('Word', width=150, anchor='w')
    tree.column('Score', width=100, anchor='center')
    tree.heading('Word', text='Word', anchor='w')
    tree.heading('Score', text='Sentiment Score', anchor='center')
    
    for word, score in data.items():
        tree.insert('', 'end', values=(word, f"{score:.2f}"))
    
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    
    return tree, scrollbar

def run_analysis():
    user_input = entry.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter some text for analysis.")
        return
    
    sentiment, score, word_scores, color = analyze_sentiment(user_input)
    
    for widget in result_frame.winfo_children():
        widget.destroy()
    for widget in plot_frame.winfo_children():
        widget.destroy()

    result_header = ttk.Label(result_frame, 
                            text=f"Overall Sentiment: {sentiment}",
                            font=('Helvetica', 14, 'bold'),
                            foreground=color)
    result_header.pack(pady=5)

    score_frame = ttk.Frame(result_frame)
    score_frame.pack(pady=10, fill='x')
    
    score_data = {
        'Compound': f"{score['compound']:.2f}",
        'Positive': f"{score['pos']:.2f}",
        'Neutral': f"{score['neu']:.2f}",
        'Negative': f"{score['neg']:.2f}"
    }
    
    score_table = ttk.Treeview(score_frame, columns=('Metric', 'Value'), show='headings', height=1)
    score_table.column('Metric', width=100, anchor='w')
    score_table.column('Value', width=100, anchor='center')
    score_table.heading('Metric', text='Metric')
    score_table.heading('Value', text='Value')
    
    for key, value in score_data.items():
        score_table.insert('', 'end', values=(key, value))
    
    score_table.pack(side='left', padx=10)

    word_frame = ttk.LabelFrame(result_frame, text="Word-level Sentiment Analysis")
    word_frame.pack(pady=10, fill='both', expand=True)
    
    table, scrollbar = create_table(word_frame, word_scores)
    table.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    fig, ax = plt.subplots(figsize=(5, 3))
    labels = ['Positive', 'Neutral', 'Negative']
    values = [score['pos'], score['neu'], score['neg']]
    colors = ['#2ecc71', '#3498db', '#e74c3c']
    
    bars = ax.bar(labels, values, color=colors)
    ax.set_ylim(0, 1)
    ax.set_title("Sentiment Distribution", fontsize=12)
    ax.set_ylabel("Proportion", fontsize=10)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom')

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

def reset():
    entry.delete("1.0", tk.END)
    for widget in result_frame.winfo_children():
        widget.destroy()
    for widget in plot_frame.winfo_children():
        widget.destroy()

def main():
    global entry, result_frame, plot_frame
    
    root = tk.Tk()
    root.title("Advanced Sentiment Analyzer")
    root.geometry("900x700")

    style = ttk.Style()
    style.configure('TFrame', background='#f0f0f0')
    style.configure('TButton', font=('Helvetica', 10))
    style.configure('Treeview', font=('Helvetica', 10), rowheight=25)
    style.configure('Treeview.Heading', font=('Helvetica', 11, 'bold'))
    
    main_frame = ttk.Frame(root)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    input_frame = ttk.LabelFrame(main_frame, text="Input Text")
    input_frame.pack(fill='x', pady=10)
    
    entry = scrolledtext.ScrolledText(input_frame, height=5, wrap=tk.WORD, font=('Helvetica', 10))
    entry.pack(fill='x', padx=5, pady=5)

    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=10)
    
    ttk.Button(button_frame, text="Analyze", command=run_analysis).pack(side='left', padx=5)
    ttk.Button(button_frame, text="Clear", command=reset).pack(side='left', padx=5)

    result_frame = ttk.Frame(main_frame)
    result_frame.pack(fill='x', pady=10)

    plot_frame = ttk.Frame(main_frame)
    plot_frame.pack(fill='both', expand=True)

    root.mainloop()
    
if __name__ == "__main__":
    main()
