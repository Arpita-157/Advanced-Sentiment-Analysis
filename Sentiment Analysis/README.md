# 📊 Sentiment Analyzer with Dashboard Function

## 📌 Project Overview

This project is a **Sentiment Analysis Tool** built using Python and Tkinter. It allows users to input text and analyzes the sentiment using **NLTK's VADER Sentiment Intensity Analyzer**. The tool provides a detailed breakdown of sentiment scores, including **word-level contributions** and a **visual representation** of sentiment distribution.

## 🚀 Features

- 📝 **User Input:** Enter any sentence for sentiment analysis.
- 📊 **Sentiment Breakdown:** Displays overall sentiment as Positive, Neutral, or Negative.
- 🔎 **Word-Level Contribution:** Shows how each word impacts sentiment.
- 📉 **Graphical Representation:** A bar chart for sentiment distribution.
- 🔄 **Reset Functionality:** Allows users to re-enter text and run new analyses.

## 🛠️ Installation

To install all required dependencies, run the following command:

```bash
pip install pandas matplotlib nltk tk
```

Additionally, download the NLTK lexicon using:

```python
import nltk
nltk.download('vader_lexicon')
```

## 🎯 Usage

Run the Python script:

```bash
python quiz.py
```

## 📌 How It Works

1. **User Input:** Type a sentence in the input field.
2. **Analysis:** The tool processes the text using NLTK's Sentiment Intensity Analyzer.
3. **Output:**
   - Displays the overall sentiment classification.
   - Shows individual word contributions.
   - Generates a bar chart for sentiment distribution.
4. **Reset Button:** Clears the input and results for new analysis.



👨‍💻 **Developed by:** Arpita Panda\
Data Scientist & Software Developer

