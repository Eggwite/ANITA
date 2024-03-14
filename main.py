#template-gen.py
from PIL import Image, ImageDraw
from PIL import ImageFont
import datetime
import random

# Set the width and height of the image
width = 700
height = 830

# Create a new RGBA image with transparent background
image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw a rectangle on the image
draw.rectangle([(0, 0), (720, 830)], fill="#0F1725")

# Set the radius and margin for the circle
radius = 40
margin = 40

# Calculate the center position of the circle
center = (radius + margin, radius + margin)

# Draw a circle on the image
draw.ellipse([(margin, margin), (radius*2 + margin, radius*2 + margin)], fill=(0, 0, 0, 0), outline=None)

# Set the width and height of the rectangle
rectangle_width = 590
rectangle_height = rectangle_width * 9 // 16

# Calculate the position of the rectangle
rectangle_position = (
    (width - rectangle_width) // 2 - 10,
    (height - rectangle_height) // 2 + 60
)

# Set the border radius for the rounded rectangle
border_radius = 15

# Draw a rounded rectangle on the image
draw.rounded_rectangle(
    [rectangle_position, (rectangle_position[0] + rectangle_width, rectangle_position[1] + rectangle_height)],
    radius=border_radius,
    fill=(0, 0, 0, 0), 
    outline=None  
)

# Open and resize the dots icon
dots_icon = Image.open("assets/dots60.png")
dots_icon = dots_icon.resize((20, 20))

# Set the position of the dots icon
dots_icon_position = (
    width - dots_icon.width - margin,
    margin
)

# Paste the dots icon onto the image
image.paste(dots_icon, dots_icon_position, mask=dots_icon)

# Define a list of profile names
profile_names = [
    "AnimeLover123",
    "OtakuGuru",
    "NarutoFanatic",
    "SaitamaSensei",
    "MangaAddict",
    "KawaiiKitten",
    "ChibiMaster",
    "CosplayQueen",
    "WeebWarrior",
    "SenpaiSlayer",
    "AnimeNinja",
    "MoeMoe",
    "SugoiSushi",
    "GeekyGamer",
    "KawaiiPotato",
    "Vicineko",
    "Hikigaya"
]

# Choose a random profile name
text = random.choice(profile_names)

# Set the position of the profile name
position = (140, 50)

# Set the color of the profile name text
text_color = (255, 255, 255)

# Set the font path, size, and style for the profile name
font_path = "assets/fonts/bold.ttf"
font_size = 27
font = ImageFont.truetype(font_path, font_size)

# Add the profile name to the image
draw.text(position, text, fill=text_color, font=font)

# Calculate the width of the profile name text
text_width = len(text) * 18
text_right = text_width + 130

# Open and resize the verified icon
verified_icon = Image.open("assets/ver96.png")
verified_icon = verified_icon.resize((30, 30))

# Set the position of the verified icon
verified_icon_position = (
    text_right,
    50
)

# Paste the verified icon onto the image
image.paste(verified_icon, verified_icon_position, mask=verified_icon)

# Add gray text below the existing text
sub_text = "@BestAnimeClips"
sub_position = (135, 88)

# Set the font path, size, and style for the gray text
sub_font_path = "assets/fonts/arial.ttf"
sub_font_size = 19  
sub_font = ImageFont.truetype(sub_font_path, sub_font_size)
sub_text_color = (128, 128, 128)  

# Add the gray text to the image
draw.text(sub_position, sub_text, fill=sub_text_color, font=sub_font)

# Define a list of comments (Yes they were AI generated)
comments = [
    "This anime clip is amazing! Just wait and watch the end, haha!", 
    "The animation in this scene is top-notch! The animators just cooked with this scene!", 
    "I can't get enough of this anime, it's so good! I wish it had more episodes!", 
    "This clip gave me the chills, can't get enough! I can't stop re-watching it!", 
    "The sound design in this scene is so epic, I wonder how long this took to make?", 
    "Man, I wish this anime had more episodes! I can't get enough of it!", 
    "This moment is pure gold! I wish I could forget it and watch it again!", 
    "I'm completely blown away by this anime clip! The visuals are stunning and the story is captivating!",
    "The attention to detail in this scene is incredible! Every frame is a work of art!",
    "I'm so invested in this anime! The plot twists keep me on the edge of my seat!",
    "This clip is so powerful! It evokes so many emotions and leaves a lasting impact!",
    "The voice acting in this scene is phenomenal! The actors bring the characters to life!",
    "I can't get over how beautiful the animation is in this anime! It's a visual feast!",
    "This moment is unforgettable! It's etched in my memory and I can't stop thinking about it!",
    "I'm addicted to this anime! I can't stop binge-watching it!",
    "The storytelling in this scene is masterful! It keeps me hooked from start to finish!",
    "This clip is a work of genius! It showcases the talent and creativity of the creators!",
    "I'm eagerly waiting for the next episode of this anime! I need to know what happens next!",
    "This anime deserves all the praise! It's a masterpiece in every aspect!",
    "This clip is pure magic! It transports me to another world and makes me believe in the power of storytelling!",
    "I'm recommending this anime to everyone I know! It's a must-watch for any anime fan!",
    "This clip is flawless! It's a testament to the dedication and hard work of the animators!",
    "I'm in awe of this anime! It's a shining example of what anime can achieve!",
    "This scene is so intense! It keeps me on the edge of my seat and leaves me wanting more!",
    "I can't get enough of this anime! It's like a drug, I crave for more!",
    "The character dynamics in this scene are fascinating! It adds depth to the story and keeps me engaged!",
    "This clip is a masterpiece of storytelling! It's a rollercoaster of emotions!",
    "I'm completely hooked on this anime! It's my new obsession!",
    "This anime clip is a work of art! It's visually stunning and emotionally impactful!",
    "I'm captivated by this scene! It's a perfect blend of action, drama, and suspense!",
    "I'm mesmerized by this anime! It's a journey of emotions and self-discovery!",
    "This clip is a gem! It's a hidden treasure that deserves more recognition!",
    "I'm enchanted by this anime! It's like a dream come true for anime lovers!",
    "This scene is so powerful! It resonates with me on a deep level and leaves me speechless!",
    "I'm completely absorbed in this anime! It's a world I never want to leave!",
    "This clip is a masterpiece of animation! It pushes the boundaries of what anime can achieve!",
    "I'm on the edge of my seat watching this scene! It's filled with suspense and surprises!",
    "I'm addicted to this anime! It's my escape from reality and I can't get enough of it!",
    "This anime clip is a work of genius! It's a testament to the creativity and talent of the creators!",
    "I'm eagerly anticipating the next episode of this anime! It's become a highlight of my week!",
    "This clip is pure perfection! It's a shining example of what anime can accomplish!",
    "I'm in love with this anime! It's captured my heart and soul!",
    "This scene is so emotional! It tugs at my heartstrings and brings tears to my eyes!",
    "I'm obsessed with this anime! It's taken over my life and I couldn't be happier!",
    "This clip is a masterpiece of storytelling! It's a journey of emotions and self-discovery!",
    "I'm completely hooked on this anime! It's my new obsession!",
    "This anime clip is a work of art! It's visually stunning and emotionally impactful!",
    "I'm captivated by this scene! It's a perfect blend of action, drama, and suspense!",
    "I'm mesmerized by this anime! It's a journey of emotions and self-discovery!",
    "This clip is a gem! It's a hidden treasure that deserves more recognition!",
    "I'm enchanted by this anime! It's like a dream come true for anime lovers!",
    "This scene is so powerful! It resonates with me on a deep level and leaves me speechless!",
    "I'm completely absorbed in this anime! It's a world I never want to leave!",
    "This clip is a masterpiece of animation! It pushes the boundaries of what anime can achieve!",
    "I'm on the edge of my seat watching this scene! It's filled with suspense and surprises!",
    "I'm addicted to this anime! It's my escape from reality and I can't get enough of it!",
    "This anime clip is a work of genius! It's a testament to the creativity and talent of the creators!",
    "I'm eagerly anticipating the next episode of this anime! It's become a highlight of my week!",
    "This clip is pure perfection! It's a shining example of what anime can accomplish!",
    "I'm in love with this anime! It's captured my heart and soul!",
    "This scene is so emotional! It tugs at my heartstrings and brings tears to my eyes!",
    "I'm obsessed with this anime! It's taken over my life and I couldn't be happier!"
]

# Choose a random comment
description_text = random.choice(comments)

# If the comment is too long, split it into multiple lines
if len(description_text) > 40:
    words = description_text.split()
    description_text = ""
    line_length = 0
    for word in words:
        if line_length + len(word) > 40:
            description_text += "\n"
            line_length = 0
        description_text += word + " "
        line_length += len(word) + 1

# Set the position of the comment text
description_position = (45, 175)

# Set the font path, size, and style for the comment text
description_font_path = "assets/fonts/arial.ttf"
description_font_size = 34  
description_font = ImageFont.truetype(description_font_path, description_font_size)
description_text_color = (255, 255, 255)  

# Add the comment text to the image
draw.text(description_position, description_text, fill=description_text_color, font=description_font)

# Generate a random number of views
seen_text = f"{random.randint(10, 10000)} views"

# Set the position of the views text
seen_position = (
    (width - rectangle_width) // 2 - 10,
    (height - rectangle_height) + 155
)

# Set the font path, size, and style for the views text
seen_font_path = "assets/fonts/arial.ttf"
seen_font_size = 27  
seen_font = ImageFont.truetype(seen_font_path, seen_font_size)
seen_text_color = (128,128,128)  

# Add the views text to the image
draw.text(seen_position, seen_text, fill=seen_text_color, font=seen_font)

# Set the text for the device used to post the tweet
post_text = "Twitter for iPhone"

# Set the position of the device text
post_position = (
    315,
    height - 105
)

# Set the font path, size, and style for the device text
post_font_path = "assets/fonts/bold.ttf"
post_font_size = 27  
post_font = ImageFont.truetype(post_font_path, post_font_size)
post_text_color = ("#205790")  

# Add the device text to the image
draw.text(post_position, post_text, fill=post_text_color, font=post_font)

# Get the current time
current_time = datetime.datetime.now().strftime("%I:%M %p")

# Set the position of the time text
time_position = (45, height - 105)

# Set the font path, size, and style for the time text
time_font_path = "assets/fonts/arial.ttf"
time_font_size = 28 
time_font = ImageFont.truetype(time_font_path, time_font_size)
time_text_color = (128, 128, 128)  

# Add the time text to the image
draw.text(time_position, current_time, fill=time_text_color, font=time_font)

# Get the current date
current_date = datetime.datetime.now().strftime("%d/%m/%y")

# Set the position of the date text
date_position = (185, height - 105)

# Set the font path, size, and style for the date text
date_font_path = "assets/fonts/arial.ttf"
date_font_size = 28  
date_font = ImageFont.truetype(date_font_path, date_font_size)
date_text_color = (128, 128, 128)  

# Add the date text to the image
draw.text(date_position, current_date, fill=date_text_color, font=date_font)

# Set the color of the line
line_color = (50, 50, 50)  

# Set the length of the line
line_length = 650

# Set the position of the line
line_position = (
    (width - line_length) // 2,
    height - 60
)

# Draw a line on the image
draw.line([(line_position[0], line_position[1]), (line_position[0] + line_length, line_position[1])], fill=line_color)

# Open and resize the stat icon
stat_icon = Image.open("assets/stat60.png")
stat_icon = stat_icon.resize((30, 30))

# Set the position of the stat icon
stat_icon_position = (
    45,
    height - 40
)

# Paste the stat icon onto the image
image.paste(stat_icon, stat_icon_position, mask=stat_icon)

# Set the text for the tweet activity
view_text = "View Tweet activity"

# Set the position of the tweet activity text
view_position = (
    95,
    height - 40
)

# Set the font path, size, and style for the tweet activity text
view_font_path = "assets/fonts/arial.ttf"
view_font_size = 27
view_font = ImageFont.truetype(view_font_path, view_font_size)
view_text_color = (128,128,128)

# Add the tweet activity text to the image
draw.text(view_position, view_text, fill=view_text_color, font=view_font)

# Set the position and radius of the dots
dot_position = (178, 740)
dot_radius = 1.2
dot_color = (128, 128, 128)

# Draw the dots on the image
draw.ellipse([(dot_position[0] - dot_radius, dot_position[1] - dot_radius), (dot_position[0] + dot_radius, dot_position[1] + dot_radius)], fill=dot_color)

dot_position = (306, 740)
dot_radius = 1.2
dot_color = (128, 128, 128)

draw.ellipse([(dot_position[0] - dot_radius, dot_position[1] - dot_radius), (dot_position[0] + dot_radius, dot_position[1] + dot_radius)], fill=dot_color)

try:
    # Save the image
    image.save("temp/overlay.png", "PNG")
    print("successfully saved image")
except Exception as e:
    raise SystemExit(e)

#compiled-post.py
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from PIL import Image, ImageDraw
import random
# Defining paths
twit_path = "temp/overlay.png"
image_path = "temp/compiled.png"
video_path = "video.mp4"
output_path = "temp/compiled-template.mp4"

# Background dimensions
back_width = 700
back_height = 830

# Create a white rectangle image
image = Image.new("RGBA", (back_width, back_height), (0, 0, 0))
draw = ImageDraw.Draw(image)
# Load the profile picture image
pfp_image_path = f"assets/pfp/{random.randint(1, 6)}.png"
pfp_image = Image.open(pfp_image_path)

# Resize the profile picture image
pfp_height = 80
pfp_width = pfp_height * pfp_image.width // pfp_image.height
pfp_image = pfp_image.resize((pfp_width, pfp_height))

# Calculate the position to place the profile picture image
pfp_position = (40, 40)

# Paste the profile picture image onto the main image
image.paste(pfp_image, pfp_position)
# Define the dimensions of the rectangle
rec_width = 590
rec_height = rec_width * 9 // 16  # Aspect ratio of 16:9

# Calculate the position of the rectangle
rectangle_position = (
    (back_width - rec_width) // 2 - 10,
    (back_height - rec_height) // 2 + 60
)

# Draw the rectangle on the image
draw.rectangle(
    [rectangle_position, (rectangle_position[0] + rec_width, rectangle_position[1] + rec_height)],
    fill=(0, 0, 0),
    outline=None
)

# Save the image
image.save(image_path)
# Load the video and resize it to fit inside the rectangle
video_clip = VideoFileClip(video_path)
# Set the frame rate of the video clip
video_clip = video_clip.set_fps(45) #play with the fps honestly
video_clip = video_clip.resize(height=rec_height)
# Adjust the video clip dimensions if necessary

video_position = (
    (back_width - video_clip.size[0]) // 2,
    (back_height - video_clip.size[1]) // 2 + 60
)
# Load the overlay image
overlay_image = ImageClip(twit_path)

# Calculate the position to place the overlay image
overlay_position = (
    (back_width - overlay_image.size[0]) // 2,
    (back_height - overlay_image.size[1]) // 2 
)

# Set the duration of the overlay image to match the video clip
overlay_image = overlay_image.set_duration(video_clip.duration)

# Create the composite clip
composite_clip = CompositeVideoClip([
    ImageClip(image_path).set_duration(video_clip.duration),
    video_clip.set_position(video_position),
    overlay_image.set_position(overlay_position)
])
print(video_clip.size)
composite_clip.save_frame("temp/frame.png") # saves the first frame
# Write the result to a file
composite_clip.write_videofile(output_path, codec='libx264')

#crop+blur+composite.py
import os
from moviepy.video.fx.all import crop
import moviepy.editor as mpy
from scipy.ndimage import gaussian_filter
from termcolor import colored
# Load the original video
orig_video_path = 'video.mp4'
clip = mpy.VideoFileClip(orig_video_path)

# Calculate the desired cropped width based on 9:16 aspect ratio
crop_width = clip.h * 9 / 16

# Calculate the x-coordinates for cropping
x1, x2 = (clip.w - crop_width) // 2, (clip.w + crop_width) // 2

# Crop the video
cropped_clip = crop(clip, x1=x1, y1=0, x2=x2, y2=clip.h)
# Remove audio from the clip
cropped_clip = cropped_clip.without_audio()
# Resize the cropped video to 1080p
cropped_clip = cropped_clip.resize((720, 1280))
cropped_clip = cropped_clip.set_fps(30)
# Export the cropped video
output_path = 'temp/cropped-video.mp4'

cropped_clip.write_videofile(output_path)

def blur(image):
    """Returns a blurred (radius=2 pixels) version of the image."""
    blurred_image = image.copy()
    for i in range(3):  # Loop over each color channel (R, G, B)
        blurred_image[..., i] = gaussian_filter(image[..., i].astype(float), sigma=6)  #Only God knows where this code got copied and pasted from
    return blurred_image

# Load the original video
orig_video_path = 'temp/cropped-video.mp4'
clip = mpy.VideoFileClip(orig_video_path)

clip_blurred = clip.fl_image(blur)

# Export the blurred video
output_path = 'temp/blurred-video.mp4'
# Check if the file already exists
clip_blurred.write_videofile(output_path)


#compile blur + overlay
def overlay_video(video_path, overlay_path, output_path):
    """Overlay the video on the main video for the entire duration."""
    # Load the main video
    main_clip = mpy.VideoFileClip(video_path)
    # Load the overlay video
    overlay_clip = mpy.VideoFileClip(overlay_path)
    # Set the duration of the overlay clip to match the main clip
    overlay_clip = overlay_clip.set_duration(main_clip.duration)
    # Set the position of the overlay clip to be centered
    overlay_clip = overlay_clip.set_position(('center', 'center'))
    # Overlay the overlay video on the main video
    final_clip = mpy.CompositeVideoClip([main_clip, overlay_clip])
    # Export the final video
    final_clip.write_videofile(output_path)
    print(colored(f"Exported video with overlay to {output_path} successfully", 'green'))

# Call the overlay_video function
video_path = 'temp/blurred-video.mp4'
overlay_path = 'temp/compiled-template.mp4'
output_path = 'video-with-overlay.mp4'
overlay_video(video_path, overlay_path, output_path)
print(colored(f"Exported video with overlay to {output_path} successfully", 'green'))
