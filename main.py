from customtkinter import *
import threading
import time
import random


root = CTk()
root.title("Random Quote Generator")
root.geometry('900x900')

header = CTkLabel(root, text="Quote Generator", font=('Helvetca', 30))
header.pack(pady=15)

l = CTkLabel(root, text="Enter the no of Quotes you want to generate:")
l.pack(pady=9)
textbox = CTkEntry(root)
textbox.pack(pady = 5)

def Gen():
    num = int(textbox.get())
    for i in range(num): 
        quotes = [
                    "The only way to do great work is to love what you do. - Steve Jobs",
                    "Life is what happens when you're busy making other plans. - John Lennon",
                    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
                    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
                    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
                    "Believe you can and you're halfway there. - Theodore Roosevelt",
                    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
                    "It does not matter how slowly you go as long as you do not stop. - Confucius",
                    "Don't cry because it's over, smile because it happened. - Dr. Seuss",
                    "Everything you can imagine is real. - Pablo Picasso",
                    "Life is either a daring adventure or nothing at all. - Helen Keller",
                    "The best way to predict the future is to create it. - Peter Drucker",
                    "The only source of knowledge is experience. - Albert Einstein",
                    "We may encounter many defeats but we must not be defeated. - Maya Angelou",
                    "Life is trying things to see if they work. - Ray Bradbury",
                    "Change your thoughts and you change your world. - Norman Vincent Peale",
                    "In the middle of difficulty lies opportunity. - Albert Einstein",
                    "The secret of getting ahead is getting started. - Mark Twain",
                    "The only impossible journey is the one you never begin. - Tony Robbins",
                    "Whatever you are, be a good one. - Abraham Lincoln",
                    "The journey of a thousand miles begins with one step. - Lao Tzu",
                    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
                    "The purpose of our lives is to be happy. - Dalai Lama",
                    "Life is not about finding yourself. Life is about creating yourself. - George Bernard Shaw",
                    "Don't wait. The time will never be just right. - Napoleon Hill",
                    "The only way to do great work is to love what you do. - Steve Jobs",
                    "Life is what happens when you're busy making other plans. - John Lennon",
                    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
                    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
                    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
                    "Believe you can and you're halfway there. - Theodore Roosevelt",
                    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
                    "It does not matter how slowly you go as long as you do not stop. - Confucius",
                    "Don't cry because it's over, smile because it happened. - Dr. Seuss",
                    "Everything you can imagine is real. - Pablo Picasso",
                    "Life is either a daring adventure or nothing at all. - Helen Keller",
                    "The best way to predict the future is to create it. - Peter Drucker",
                    "The only source of knowledge is experience. - Albert Einstein",
                    "We may encounter many defeats but we must not be defeated. - Maya Angelou",
                    "Life is trying things to see if they work. - Ray Bradbury",
                    "Change your thoughts and you change your world. - Norman Vincent Peale",
                    "In the middle of difficulty lies opportunity. - Albert Einstein",
                    "The secret of getting ahead is getting started. - Mark Twain",
                    "The only impossible journey is the one you never begin. - Tony Robbins",
                    "Whatever you are, be a good one. - Abraham Lincoln",
                    "The journey of a thousand miles begins with one step. - Lao Tzu",
                    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
                    "The purpose of our lives is to be happy. - Dalai Lama",
                    "Life is not about finding yourself. Life is about creating yourself. - George Bernard Shaw",
                    "Don't wait. The time will never be just right. - Napoleon Hill",
                    "The only way to do great work is to love what you do. - Steve Jobs",
                    "Life is what happens when you're busy making other plans. - John Lennon",
                    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
                    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
                    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
                    "Believe you can and you're halfway there. - Theodore Roosevelt",
                    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
                    "It does not matter how slowly you go as long as you do not stop. - Confucius",
                    "Don't cry because it's over, smile because it happened. - Dr. Seuss",
                    "Everything you can imagine is real. - Pablo Picasso",
                    "Life is either a daring adventure or nothing at all. - Helen Keller",
                    "The best way to predict the future is to create it. - Peter Drucker",
                    "The only source of knowledge is experience. - Albert Einstein",
                    "We may encounter many defeats but we must not be defeated. - Maya Angelou",
                    "Life is trying things to see if they work. - Ray Bradbury",
                    "Change your thoughts and you change your world. - Norman Vincent Peale",
                    "In the middle of difficulty lies opportunity. - Albert Einstein",
                    "The secret of getting ahead is getting started. - Mark Twain",
                    "The only impossible journey is the one you never begin. - Tony Robbins",
                    "Whatever you are, be a good one. - Abraham Lincoln",
                    "The journey of a thousand miles begins with one step. - Lao Tzu",
                    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
                    "The purpose of our lives is to be happy. - Dalai Lama",
                    "Life is not about finding yourself. Life is about creating yourself. - George Bernard Shaw",
                    "Don't wait. The time will never be just right. - Napoleon Hill",
                    "The only way to do great work is to love what you do. - Steve Jobs",
                    "Life is what happens when you're busy making other plans. - John Lennon",
                    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
                    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
                    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
                    "Believe you can and you're halfway there. - Theodore Roosevelt",
                    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
                    "It does not matter how slowly you go as long as you do not stop. - Confucius",
                    "Don't cry because it's over, smile because it happened. - Dr. Seuss",
                    "Everything you can imagine is real. - Pablo Picasso",
                    "Life is either a daring adventure or nothing at all. - Helen Keller",
                    "The best way to predict the future is to create it. - Peter Drucker",
                    "The only source of knowledge is experience. - Albert Einstein",
                    "We may encounter many defeats but we must not be defeated. - Maya Angelou",
                    "Life is trying things to see if they work. - Ray Bradbury",
                    "Change your thoughts and you change your world. - Norman Vincent Peale",
                    "In the middle of difficulty lies opportunity. - Albert Einstein",
                    "The secret of getting ahead is getting started. - Mark Twain",
                    "The only impossible journey is the one you never begin. - Tony Robbins",
                    "Whatever you are, be a good one. - Abraham Lincoln",
                    "The journey of a thousand miles begins with one step. - Lao Tzu",
                    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
                    "The purpose of our lives is to be happy. - Dalai Lama",
                    "Life is not about finding yourself. Life is about creating yourself. - George Bernard Shaw",
                    "Don't wait. The time will never be just right. - Napoleon Hill"
                ]                               #list of Quotes

        
        label_quote = CTkLabel(frame , text=random.choice(quotes))
        label_quote.pack(pady=7)

        if num >= 20:
           time.sleep(0)
        else:
            time.sleep(2)  #for 2 Second Time Delay
    
    label.configure(text="Done!")


def run_thread():
  t = threading.Thread(target=Gen)
  t.start()

label = CTkLabel(root, text="Click the button To generate Random Quotes!")
label.pack(pady=6)

btn = CTkButton(root , text="Generate Quotes!", command=run_thread) # 
btn.pack(pady = 10)

frame = CTkScrollableFrame(root, width=850, height=850, corner_radius=15)
frame.pack(pady=10)

root.mainloop()