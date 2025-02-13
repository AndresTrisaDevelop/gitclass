import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

# Create a new figure and axis
fig, ax = plt.subplots(figsize=(10, 12))
ax.set_xlim(0, 6)
ax.set_ylim(0, 12)
ax.axis('off')

# Function to create a process box
def create_box(text, xy, width=2, height=0.5, boxstyle="round,pad=0.3", color="lightblue"):
    box = mpatches.FancyBboxPatch(xy, width, height, boxstyle=boxstyle, linewidth=1, edgecolor="black", facecolor=color)
    ax.add_patch(box)
    ax.text(xy[0] + width/2, xy[1] + height/2, text, ha='center', va='center', fontsize=10, color="black")

# Function to create an arrow
def create_arrow(start, end):
    ax.add_patch(FancyArrowPatch(start, end, connectionstyle="arc3,rad=0", arrowstyle='->', mutation_scale=15))

# Coordinates for each step
coords = {
    "Start": (3, 11),
    "Main Dashboard": (3, 9),
    "Records Section": (1, 7),
    "Comparison": (3, 7),
    "Settings": (5, 7),
    "Record Entry Process": (1, 5),
    "Comparison Process": (3, 5),
    "Metadata Management": (5, 5),
    "Data Mode Selection": (1, 3),
    "Feedback Submission": (3, 3),
    "End": (3, 1),
}

# Create boxes
create_box("Start (User Login)", coords["Start"])
create_box("Main Dashboard", coords["Main Dashboard"])
create_box("Records Section", coords["Records Section"], color="lightgreen")
create_box("Comparison", coords["Comparison"], color="lightgreen")
create_box("Settings", coords["Settings"], color="lightgreen")
create_box("Record Entry Process", coords["Record Entry Process"])
create_box("Comparison Process", coords["Comparison Process"])
create_box("Metadata Management", coords["Metadata Management"])
create_box("Data Mode Selection", coords["Data Mode Selection"])
create_box("Feedback Submission", coords["Feedback Submission"])
create_box("End", coords["End"])

# Create arrows
create_arrow((3.5, 10.7), (3.5, 9.3))  # Start to Main Dashboard
create_arrow((3, 8.7), (1.5, 7.5))     # Main Dashboard to Records Section
create_arrow((3, 8.7), (3, 7.5))       # Main Dashboard to Comparison
create_arrow((3, 8.7), (4.5, 7.5))     # Main Dashboard to Settings
create_arrow((1, 6.7), (1, 5.5))       # Records Section to Record Entry Process
create_arrow((3, 6.7), (3, 5.5))       # Comparison to Comparison Process
create_arrow((5, 6.7), (5, 5.5))       # Settings to Metadata Management
create_arrow((1, 4.7), (1, 3.5))       # Record Entry Process to Data Mode Selection
create_arrow((3, 4.7), (3, 3.5))       # Comparison Process to Feedback Submission
create_arrow((1, 2.7), (3, 1.5))       # Data Mode Selection to End
create_arrow((3, 2.7), (3, 1.5))       # Feedback Submission to End

# Show plot
plt.show()
