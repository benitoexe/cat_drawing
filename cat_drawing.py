import DrawingPanel

panel = DrawingPanel.DrawingPanel(400, 400)
panel.set_background("black")

panel.fill_oval(100, 100, 200, 200, "orange")
panel.fill_oval(140, 150, 50, 50, "white")
panel.fill_oval(210, 150, 50, 50, "white")
panel.fill_oval(140, 150, 30, 30, "black")
panel.fill_oval(210, 150, 30, 30, "black")
panel.fill_polygon(115, 150, 110, 65, 175, 110, "orange")
panel.fill_polygon(230, 110, 280, 139, 280, 65, "orange")

panel.fill_polygon(200, 250, 180, 215, 225, 215, "pink")
panel.draw_line(250,230,350,200, "white")
panel.draw_line(250,230,350,230, "white")
panel.draw_line(250,230,350,250, "white")

(123,130,113,70,150,100

