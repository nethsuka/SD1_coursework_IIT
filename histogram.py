from graphics import *

def draw_histrogram(total, progress_count, trailer_count, retriever_count, exclude_count):

        win = GraphWin("Histogram", 505, 420)
        win.setBackground(color_rgb(224, 224, 224))

        #============ Title of the graphs ==================================

        title_word= Text(Point(120,35),"Histogram Results")
        title_word.setStyle("bold")
        title_word.setTextColor(color_rgb(64, 64, 64))
        title_word.setSize(15) # 5- 36 range
        title_word.draw(win)

        #============== count and graphics of progress outcome ==============

        progress_persentage = (315*progress_count)/total

        Rectangle1_word= Text(Point(105,(315-progress_persentage)-10),progress_count) #Progress_count
        Rectangle1_word.setStyle("bold")
        Rectangle1_word.setTextColor(color_rgb(96, 96, 96))
        Rectangle1_word.setSize(12)
        Rectangle1_word.draw(win)

        Rectangle1 = Rectangle(Point(60,350), Point(150,315-progress_persentage))
        Rectangle1.setFill(color_rgb(153, 225, 153))
        Rectangle1.draw(win)

        #============== count and graphics of trailer outcome ==============

        trailer_persentage = (315*trailer_count)/total

        Rectangle2_word = Text(Point(205,(315-trailer_persentage)-10),trailer_count) #Trailer_count
        Rectangle2_word.setStyle("bold")
        Rectangle2_word.setTextColor(color_rgb(96, 96, 96))
        Rectangle2_word.setSize(12)
        Rectangle2_word.draw(win)

        Rectangle2 = Rectangle(Point(160,350), Point(250,315-trailer_persentage))
        Rectangle2.setFill(color_rgb(143,188,143))
        Rectangle2.draw(win)

        #============== count and graphics of retriever outcome ==============

        retriever_percentage = (315*retriever_count)/total

        Rectangle3_word= Text(Point(305,(315-retriever_percentage)-10),retriever_count) #Retriever_count
        Rectangle3_word.setStyle("bold")
        Rectangle3_word.setTextColor(color_rgb(96, 96, 96))
        Rectangle3_word.setSize(12)
        Rectangle3_word.draw(win)

        Rectangle3 = Rectangle(Point(260,350), Point(350,315-retriever_percentage))
        Rectangle3.setFill(color_rgb(189, 183, 107))
        Rectangle3.draw(win)

        #============== count and graphics of exclude outcome ==============

        exclude_percentage = (315*exclude_count)/total

        Rectangle4_word= Text(Point(406,(315-exclude_percentage)-10),exclude_count) #Excluded_count
        Rectangle4_word.setStyle("bold")
        Rectangle4_word.setTextColor(color_rgb(96, 96, 96))
        Rectangle4_word.setSize(12)
        Rectangle4_word.draw(win)

        Rectangle4 = Rectangle(Point(360,350), Point(450,315-exclude_percentage))
        Rectangle4.setFill(color_rgb(216,191,216))
        Rectangle4.draw(win)

        #============== horizontal line and words ===========================

        aline  = Line(Point(30,350), Point(480,350)) # line
        aline.draw(win)
        aline.setArrow("last")

        Progress_word= Text(Point(105,360),"Progress") #Progress_word
        Progress_word.setStyle("bold")
        Progress_word.setTextColor(color_rgb(96, 96, 96))
        Progress_word.setSize(12)
        Progress_word.draw(win)

        Trailer_word = Text(Point(205,360),"Trailer") #Trailer_word
        Trailer_word.setStyle("bold")
        Trailer_word.setTextColor(color_rgb(96, 96, 96))
        Trailer_word.setSize(12)
        Trailer_word.draw(win)

        Retriever_word= Text(Point(305,360),"Retriever") #Retriever_word
        Retriever_word.setStyle("bold")
        Retriever_word.setTextColor(color_rgb(96, 96, 96))
        Retriever_word.setSize(12)
        Retriever_word.draw(win)

        Excluded_word= Text(Point(406,360),"Excluded") #Excluded_word
        Excluded_word.setStyle("bold")
        Excluded_word.setTextColor(color_rgb(96, 96, 96))
        Excluded_word.setSize(12)
        Excluded_word.draw(win)

        #============== Display total ====================================

        total_number = str(total) + " outcomes in total"

        a= Text(Point(160,395),total_number)
        a.setStyle("bold")
        a.setTextColor(color_rgb(96, 96, 96))
        a.setSize(14)
        a.draw(win)

        win.getMouse() # Pause to view result
        win.close()    # Close window when done


total = int(input("enter total :"))
progress_count = int(input("enter progress count :"))
trailer_count = int(input("enter trailer count :"))
retriever_count = int(input("enter retriever count :"))
exclude_count = int(input("enter exclude count :"))

draw_histrogram(total, progress_count, trailer_count, retriever_count, exclude_count)