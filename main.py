from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

BACKGROUND_COLOR = "#B1DDC6"


class WatermarkApp:

    def __init__(self, master):
        self.image_file = None
        self.master = master
        master.title("Watermark App")
        canvas = Canvas(width=300, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
        canvas.grid(column=0, row=0, rowspan=5)

        self.image_label = Label(master, text="Select an image:",  bg=BACKGROUND_COLOR, font=("arial", 10, "bold"))
        self.image_label.grid(column=0, row=0)

        self.select_button = Button(master, text="Select", command=self.select_image)
        self.select_button.grid(column=0, row=1)

        self.watermark_label = Label(master, text="Enter watermark text:", bg=BACKGROUND_COLOR, font=("arial", 10, "bold"))
        self.watermark_label.grid(column=0, row=2)

        self.watermark_entry = Entry(master)
        self.watermark_entry.grid(column=0, row=3)

        self.save_button = Button(master, text="Save", command=self.save_watermarked_image)
        self.save_button.grid(column=0, row=4)

    def select_image(self):
        self.image_file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;8.jpeg;*.png")])
        if self.image_file:
            self.image_label.config(text=f"Image selected:\n{self.image_file}")
        else:
            self.image_label.config(text="No image selected.")

    def save_watermarked_image(self):
        if hasattr(self, "image_file"):
            image = Image.open(self.image_file)
            draw = ImageDraw.Draw(image)
            width, height = image.size
            font_size = min(width, height) // 20
            font = ImageFont.truetype("arial.ttf", font_size)
            text = self.watermark_entry.get()
            text_width, text_height = draw.textsize(text, font=font)
            x = width - text_width - font_size
            y = height - text_height - font_size
            draw.text((x, y), text, fill=(255, 255, 255, 128), font=font)
            save_file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "8.png")])
            if save_file:
                image.save(save_file)
                self.image_label.config(text=f"Watermarked image saved:\n{save_file}")
            else:
                self.image_label.config(text="No image selected.")


root = Tk()
root.config(padx=20, pady=20, width=800, height=800, bg=BACKGROUND_COLOR)
app = WatermarkApp(root)
root.mainloop()
