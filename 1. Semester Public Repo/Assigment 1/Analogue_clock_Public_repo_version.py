from datetime import datetime
import pygame
import math
pygame.init()

# Boilerplate requirements
Width, Height = 900, 700
screen = pygame.display.set_mode((Width, Height))
ScreenCenter = (Width/2, Height/2)

pygame.display.set_caption("Analogue Clock")
ProgramRun = True
FPSCap = pygame.time.Clock()

# Initialising datetime so i can fetch current system time
DateTimeINIT = datetime.now()
seconds = DateTimeINIT.second
minutes = DateTimeINIT.minute
hours = DateTimeINIT.hour

# Analogue clock requires a few variables
radius = 300
rotation = 360
Defualt_thickness = 5

MinuteHandLenghth = radius * 0.5
SecondsHandLength = radius * 0.2
HoursHandLength = radius   * 0.7

# A few colors to get started
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# Font system
font = pygame.font.Font(None, 40)
textfont = pygame.font.SysFont("monospace", 30)




# A function to calculate line sizes based on importance
def draw_lines():
    for line in range (60):
        angle = line/60 * (2 * math.pi)
        CircleEdgeX = ScreenCenter[0] + radius * math.cos(angle - math.pi/2)
        CircleEdgeY = ScreenCenter[1] + radius * math.sin(angle - math.pi/2)
        CircleLinePoints = (CircleEdgeX, CircleEdgeY)

        if line % 5 == 0:
             line_length = radius - 40
             
        else:
             line_length = radius - 20

        num_x = ScreenCenter[0] + line_length * math.cos(angle - math.pi / 2)
        num_y = ScreenCenter[1] + line_length * math.sin(angle - math.pi / 2)
   
        pygame.draw.aaline(screen, white, (num_x, num_y), CircleLinePoints, 5)

        
# converts the 
def ChronologyConversion():
    now = datetime.now()

    SecondsAngle = math.radians((now.second / 60) * rotation)
    MinutesAngle = math.radians((now.minute / 60) * rotation + (now.second / 60) * 6)
    HoursAngle = math.radians((now.hour % 12 / 12) * rotation + (now.minute / 60) * 30)

    return SecondsAngle, MinutesAngle, HoursAngle


# The length of the clock hands need to be calculated
def hand_lengths(SecondsAngle, MinutesAngle, HoursAngle):
    HourHandX = ScreenCenter[0] + HoursHandLength * math.cos(HoursAngle - math.pi / 2)
    HourHandY = ScreenCenter[1] + HoursHandLength * math.sin(HoursAngle - math.pi / 2)
    HourHandXY = (HourHandX, HourHandY)

    MinuteHandX = ScreenCenter[0] + MinuteHandLenghth * math.cos(MinutesAngle - math.pi / 2)
    MinuteHandY = ScreenCenter[1] + MinuteHandLenghth * math.sin(MinutesAngle - math.pi / 2)
    MinuteHandXY = (MinuteHandX, MinuteHandY)


    SecondHandX = ScreenCenter[0] + SecondsHandLength * math.cos(SecondsAngle - math.pi / 2)
    SecondHandY = ScreenCenter[1] + SecondsHandLength * math.sin(SecondsAngle - math.pi / 2)
    SecondHandXY = (SecondHandX, SecondHandY)

    return HourHandXY, MinuteHandXY, SecondHandXY

# Draw the numbers
def Draw_Number():
    Distance = radius - 65
    for number in range(12):
        angle = (number / 12) * (2 * math.pi) - math.pi / 2 

        CircleEdgeX = ScreenCenter[0] + Distance * math.cos(angle)
        CircleEdgeY = ScreenCenter[1] + Distance * math.sin(angle)
        CircleEdgeXY = (CircleEdgeX, CircleEdgeY)

        if number != 0:
            hour_text = textfont.render(str(number), True, white)
        else:
            hour_text = textfont.render(str(12), True, white)

        Numbers = hour_text.get_rect(center=(CircleEdgeXY[0], CircleEdgeXY[1]))
        screen.blit(hour_text, Numbers.topleft)


        
        
        

# Prepping over, running the program
while ProgramRun:
    screen.fill(black)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ProgramRun = False
    
    HoursAngle, MinutesAngle, SecondsAngle = ChronologyConversion()
    HourHandXY, MinuteHandXY, SecondsHandXY = hand_lengths(SecondsAngle, MinutesAngle, HoursAngle)


    pygame.draw.circle(screen, white, ScreenCenter, radius, 5)
    draw_lines()
    Draw_Number()


    pygame.draw.aaline(screen, red, ScreenCenter, HourHandXY, 5)
    pygame.draw.aaline(screen, white, ScreenCenter, MinuteHandXY, 5)
    pygame.draw.aaline(screen, white, ScreenCenter, SecondsHandXY, 3)

    pygame.display.flip()
    FPSCap.tick(60)
    

pygame.quit()