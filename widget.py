from mosaico import widget, colors
import datetime

fontName = "10x20"
timeHeight = 20

# Create text for hours
hourText = widget.createText()
hourText.setFont(fontName)
hourText.moveTo(8, timeHeight)  

# Create text for colon
colonText = widget.createText()
colonText.setFont(fontName)
colonText.setColor(colors.red)
colonText.moveTo(26, timeHeight) 

# Create text for minutes
minuteText = widget.createText()
minuteText.setFont(fontName)
minuteText.moveTo(35, timeHeight)  

upRect = widget.createRectangle()
upRect.setSize(64,2)
upRect.translateYBy(timeHeight-2)

downRect = widget.createRectangle()
downRect.setSize(64,2)
downRect.translateYBy(timeHeight+19)

# Variable to keep track of the colon visibility state
colon_visible = True

def loop():
  global colon_visible
  
  current_time = datetime.datetime.now()
  hourText.setText(current_time.strftime("%H"))
  minuteText.setText(current_time.strftime("%M"))
  
  # Toggle the colon visibility
  if colon_visible:
    colonText.setText(":")
  else:
    colonText.setText("")
  
  # Update colon visibility state
  colon_visible = not colon_visible