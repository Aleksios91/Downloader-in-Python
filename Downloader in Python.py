import urllib.request
import requests
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL
from playwright.sync_api import sync_playwright
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


def simple_download(url, filename):
    try:
        print(f"Downloading from: {url}")
        
        # Create a request with a fake User-Agent (so some sites won't block you)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        # Open the URL and read the content
        with urllib.request.urlopen(req) as response:
            content = response.read()
        
        # Save it to a file
        with open(filename, 'wb') as f:
            f.write(content)
        
        print(f"Saved as: {filename}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
        
def video_download(url, path):
    try:
        print(f"Downloading from: {url}")
        ydl_opts = {'outtmpl': path, 'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'}   # Format of the downloaded file
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])   # Downloads it via URL inputted
        print(f"YouTube video saved to {path}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

   

   
        
def dynamic_page_download(url,save_path):
    try:
        with open(save_path, 'w') as f:
            f.write(f"[InternetShortcut]\nURL={url}\n")   # Uhmm,this one is kinda irrelevant chunk of code.  Specifically; f.write(f"[InternetShortcut]\nURL={url}\n"). It is supposed to download an HTML file with link provided in the text once you open it but...now it does even better job, puts you straight into the webpage once you download it.
        print(f"Link saved: {save_path}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    


# Tkinter GUI (Graphic User Interface)
Downloader=tk.Tk()
Downloader.title("Downloader")
Downloader.geometry ("1024x768")
Downloader.resizable(False, False)

# Text and entry box
text_label= tk.Label(Downloader, text="Enter URL:")
text_label.pack (pady=(30,5))
text_entry=tk.Entry(Downloader, width=50)
text_entry.pack ()

def start_download(): 
    url=text_entry.get()  # Ready your text input
    if not url:
        messagebox.showwarning ("Warning" , "Please enter a URL.")
        return
    
    if "youtube.com" in url or "youtu.be" in url:
        path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 video","*.mp4")])  # Asks you where to save it, in this specific format.
        if not path:
            print("Download canceled.")
            return
        success = video_download(url, path)

    elif url.endswith((".html", ".htm", ".txt", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf")):
        ext = url.split(".")[-1]
        path = filedialog.asksaveasfilename(defaultextension=f".{ext}",
                                            filetypes=[(f"{ext.upper()} file", f"*.{ext}")])
        if not path:
            print("Download canceled.")
            return
        success = simple_download(url, path)

    else:
        path = filedialog.asksaveasfilename(defaultextension=".url")
        if not path:
            print("Download canceled.")
            return
        success = dynamic_page_download(url, path)

    if success:
        messagebox.showinfo("Success", "Download process finished successfully!")
    else:
        messagebox.showwarning("Failed", "The download failed or was canceled.")


# Downloader Button
download_button=tk.Button(Downloader, text="Download",command=start_download)
download_button.pack(pady=40)



Downloader.mainloop()
