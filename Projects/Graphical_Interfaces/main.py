import tkinter as tk
from tkinter import colorchooser, simpledialog, filedialog
from PIL import Image, ImageDraw, ImageGrab, ImageTk
import io
import os

ghostscript_path = r'C:\Program Files\gs\gs10.02.1\bin\gswin64c.exe'
os.environ['PATH'] = '{};{}'.format(os.environ.get('PATH', ''), os.path.dirname(ghostscript_path))


class ShapeType:
    PENCIL = 0
    ERASER = 1
    RECTANGLE = 2
    CIRCLE = 3
    LINE = 4

class Shape:
    def __init__(self, start_x, start_y, end_x, end_y, outline, width):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.outline = outline
        self.width = width

    def draw(self, draw):
        pass

class Rectangle(Shape):
    def draw(self, draw):
        draw.rectangle((self.start_x, self.start_y, self.end_x, self.end_y), outline=self.outline, width=self.width)

class Circle(Shape):
    def draw(self, draw):
        draw.ellipse((self.start_x, self.start_y, self.end_x, self.end_y), outline=self.outline, width=self.width)

class Line(Shape):
    def draw(self, draw):
        draw.line((self.start_x, self.start_y, self.end_x, self.end_y), fill=self.outline, width=self.width)

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expanded Paint App")

        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.pen_color = "black"
        self.brush_size = 2
        self.selected_tool = tk.StringVar(value="pencil")

        # Initialize shape variables
        self.start_x = None
        self.start_y = None
        self.current_shape = None
        self.shapes = []
        
        #  status bar
        self.status_bar = tk.Label(root, text="Brush Size: {} | Color: {}".format(self.brush_size, self.pen_color),
                                   bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        #  menu bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        #  track of drawing actions
        self.drawing_actions = []
        self.current_action_index = -1

        #  Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)

        #  File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Save", command=self.save_drawing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.destroy)

        #  Options menu
        self.options_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Options", menu=self.options_menu)

        #  Drawing Tools submenu
        drawing_tools_menu = tk.Menu(self.options_menu, tearoff=0)
        self.options_menu.add_cascade(label="Drawing Tools", menu=drawing_tools_menu)

        drawing_tools = ["pencil", "eraser"]
        for tool in drawing_tools:
            drawing_tools_menu.add_radiobutton(label=tool.capitalize(), variable=self.selected_tool,
                                               value=tool, command=self.setup_tool)

        #  Shape Tools submenu
        shape_tools_menu = tk.Menu(self.options_menu, tearoff=0)
        self.options_menu.add_cascade(label="Shape Tools", menu=shape_tools_menu)

        shape_tools = ["line", "rectangle", "circle"]
        for tool in shape_tools:
            shape_tools_menu.add_radiobutton(label=tool.capitalize(), variable=self.selected_tool,
                                             value=tool, command=self.setup_tool)

        #  Options submenu
        options_submenu = tk.Menu(self.options_menu, tearoff=0)
        self.options_menu.add_cascade(label="Options", menu=options_submenu)
        options_submenu.add_command(label="Choose Color", command=self.choose_color)
        options_submenu.add_command(label="Brush Size", command=self.choose_brush_size)

        #  mouse events
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.continue_drawing)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def save_drawing_action(self):
        image = Image.new("RGBA", (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)

        # Capture the current content of the canvas
        ps_data = self.canvas.postscript(colormode="color", pagewidth=image.width, pageheight=image.height)
        img = Image.open(io.BytesIO(ps_data.encode("utf-8")))

        # Paste the captured content onto the new image
        image.paste(img, (0, 0))

        self.drawing_actions.append(image)

        # Update current action index
        self.current_action_index += 1

    def undo(self):
        if self.current_action_index > 0:
            self.current_action_index -= 1
            self.load_drawing_action()

    def redo(self):
        if self.current_action_index < len(self.drawing_actions) - 1:
            self.current_action_index += 1
            self.load_drawing_action()

    def load_drawing_action(self):
        # Load the drawing action at the current index
        if 0 <= self.current_action_index < len(self.drawing_actions):
            self.canvas.delete("all")

            # Convert Image to PhotoImage
            photo_image = ImageTk.PhotoImage(self.drawing_actions[self.current_action_index])

            # Create image on the canvas
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)

            # Keep a reference to avoid garbage collection
            self.canvas.photo = photo_image

    def save_drawing(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"),
                                                                                     ("All files", "*.*")])

        if file_path:
            try:
                self.root.update()
                x = self.root.winfo_rootx()
                y = self.root.winfo_rooty()
                x1 = x + self.canvas.winfo_width()
                y1 = y + self.canvas.winfo_height()
                ImageGrab.grab(bbox=(x, y, x1, y1)).save(file_path, format="png")

                print(f"Drawing saved successfully to {file_path}")

            except Exception as e:
                print(f"Error saving the drawing: {e}")

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        self.pen_color = color
        self.update_status_bar()

    def choose_brush_size(self):
        size = simpledialog.askinteger("Brush Size", "Enter brush size:", parent=self.root, minvalue=1)
        if size is not None:
            self.brush_size = size
            self.update_status_bar()

    def setup_tool(self):
        if self.selected_tool.get() == "eraser":
            self.pen_color = "white"
        else:
            self.pen_color = "black"  # Reset pen color for other tools
        self.update_status_bar()

    def start_drawing(self, event):
        self.start_x, self.start_y = event.x, event.y

        if self.selected_tool.get() != "pencil":
            self.current_shape = self.create_shape()

    def continue_drawing(self, event):
        if self.selected_tool.get() != "pencil" and self.current_shape:
            self.canvas.coords(self.current_shape, self.start_x, self.start_y, event.x, event.y)
        elif self.selected_tool.get() == "pencil" or self.selected_tool.get() == "eraser":
            self.draw_pencil()

    def stop_drawing(self, event):
        if self.selected_tool.get() != "pencil" and self.current_shape:
            # Save shape information to the list
            self.shapes.append(self.current_shape)
            self.current_shape = None

        # Save the drawing action
        self.save_drawing_action()

    def draw_pencil(self):
        x, y = self.root.winfo_pointerxy()
        x -= self.root.winfo_rootx()
        y -= self.root.winfo_rooty()
        self.canvas.create_oval(x, y, x + self.brush_size, y + self.brush_size, fill=self.pen_color,
                                outline=self.pen_color)
        self.save_drawing_action()

    def create_shape(self):
        if self.selected_tool.get() == "rectangle":
            return self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y,
                                                outline=self.pen_color, width=self.brush_size)
        elif self.selected_tool.get() == "circle":
            return self.canvas.create_oval(self.start_x, self.start_y, self.start_x, self.start_y,
                                            outline=self.pen_color, width=self.brush_size)
        elif self.selected_tool.get() == "line":
            return self.canvas.create_line(self.start_x, self.start_y, self.start_x, self.start_y,
                                           fill=self.pen_color, width=self.brush_size)
        else:
            return None

    def update_status_bar(self):
        self.status_bar.config(text="Brush Size: {} | Color: {}".format(self.brush_size, self.pen_color))

if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()
