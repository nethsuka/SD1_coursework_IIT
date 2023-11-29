from graphics import *

# check whether that the entered number is in valid range
def is_valid(marks,grade):
    while marks not in range(0, 121, 20):
        print("Out of range." + "\n")
        if grade=="pass":
            marks = int(input("Please enter your credits at pass :"))
        elif grade=="defer":
            marks = int(input("Please enter your credit at defer :"))
        else:
            marks = int(input("Please enter your credit at fail :"))
    return marks
    

# check whether that the entered value is 'y' or 'n'  
def is_valid_continuation(continue_result, method):
    if method == 'login':
        while continue_result not in ["s","t","S","T"]:
            print("Invalid input, Please enter s or t !" + "\n")
            continue_result = input("Enter the login method s/t :")
    else:
        while continue_result not in ["y","q","Y","Q"]:
            print("Invalid input, Please enter y or q !" + "\n")
            continue_result = input("Enter 'y' for yes or 'q' to quit and view results :")
    valid_continue_result = continue_result.lower()
    return valid_continue_result

# drawing histogram
def draw_histrogram(progress_count, trailer_count, retriever_count, exclude_count):

    total = progress_count + trailer_count + retriever_count + exclude_count

    try:
        # text styles
        def draw_txt(object_name):
            object_name.setStyle("bold")
            object_name.setTextColor(color_rgb(96, 96, 96))
            object_name.setSize(12)
            object_name.draw(win)

        win = GraphWin("Histogram", 505, 420)
        win.setBackground(color_rgb(224, 224, 224))

        #============ Title of the graphs ==================================

        title_word= Text(Point(120,35),"Histogram Results")
        title_word.setStyle("bold")
        title_word.setTextColor(color_rgb(64, 64, 64))
        title_word.setSize(15) # 5- 36 range
        title_word.draw(win)

        #============== count and graphics of progress outcome ==============
        
        progress_persentage = (350*progress_count)/total

        Rectangle1_word= Text(Point(105,(350-progress_persentage)-10),progress_count) #Progress_word
        draw_txt(Rectangle1_word)

        Rectangle1 = Rectangle(Point(60,350), Point(150,350-progress_persentage))
        Rectangle1.setFill(color_rgb(153, 225, 153))
        Rectangle1.draw(win)

        #============== count and graphics of trailer outcome ==============

        trailer_persentage = (350*trailer_count)/total

        Rectangle2_word = Text(Point(205,(350-trailer_persentage)-10),trailer_count) #Trailer_word
        draw_txt(Rectangle2_word)

        Rectangle2 = Rectangle(Point(160,350), Point(250,350-trailer_persentage))
        Rectangle2.setFill(color_rgb(143,188,143))
        Rectangle2.draw(win)

        #============== count and graphics of retriever outcome ==============

        retriever_percentage = (350*retriever_count)/total

        Rectangle3_word= Text(Point(305,(350-retriever_percentage)-10),retriever_count) #Retriever_word
        draw_txt(Rectangle3_word)

        Rectangle3 = Rectangle(Point(260,350), Point(350,350-retriever_percentage))
        Rectangle3.setFill(color_rgb(189, 183, 107))
        Rectangle3.draw(win)

        #============== count and graphics of exclude outcome ==============

        exclude_percentage = (350*exclude_count)/total

        Rectangle4_word= Text(Point(406,(350-exclude_percentage)-10),exclude_count) #Excluded_word
        draw_txt(Rectangle4_word)

        Rectangle4 = Rectangle(Point(360,350), Point(450,350-exclude_percentage))
        Rectangle4.setFill(color_rgb(216,191,216))
        Rectangle4.draw(win)

        #============== horizontal line and words ===========================

        aline  = Line(Point(30,350), Point(480,350)) # line
        aline.draw(win)
        aline.setArrow("last")

        Progress_word= Text(Point(105,360),"Progress") #Progress_word
        draw_txt(Progress_word)
        Trailer_word = Text(Point(205,360),"Trailer") #Trailer_word
        draw_txt(Trailer_word)
        Retriever_word= Text(Point(305,360),"Retriever") #Retriever_word
        draw_txt(Retriever_word)
        Excluded_word= Text(Point(406,360),"Excluded") #Excluded_word
        draw_txt(Excluded_word)

        #============== Display total ====================================

        total_number = str(total) + " outcomes in total"

        a= Text(Point(160,395),total_number)
        a.setStyle("bold")
        a.setTextColor(color_rgb(96, 96, 96))
        a.setSize(14)
        a.draw(win)

        win.getMouse() # Pause to view result
        win.close()    # Close window when done
    except GraphicsError:
            pass
    

# decide the progression outcome
def get_progression_outcome(pass_mark, defer_mark, fail_mark):

    if (pass_mark + defer_mark + fail_mark)  != 120:
        return "Total incorrect."
    else:
        if pass_mark == 120:
            return "Progress"
        elif pass_mark == 100:
            return "Progress (module trailer)"
        elif fail_mark < 80:
            return "Module retriever"
        else:
            return "Exclude"
        
# Printing entered data when program quit
def display_data_list(progressed_datalist):
    print("Part 2:")
    for i in progressed_datalist:
            print(f"{i[0]} - {i[1]}, {i[2]}, {i[3]}")

# Geting a valid intiger
def enter_value(value):
    while True:
        try:
            if value == "pass_mark":
                mark = int(input("Please enter your credits at pass :"))
                valid_mark = is_valid(mark,grade = "pass")
            elif value == "defer_mark":
                mark = int(input("Please enter your credit at defer :"))
                valid_mark = is_valid(mark,grade = "defer")
            else:
                mark = int(input("Please enter your credit at fail :"))
                valid_mark = is_valid(mark,grade = "fail")
        except ValueError:
            print("Integer required"+ "\n")
        else:
            break
    return valid_mark

    

#program starts from here
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
progressed_datalist = []

print("\n"+"============ Enter 's' to login as a student and 't' to login as a staff member ============"+"\n")
login_method = input("Enter the login method s/t :")
valid_login_method = is_valid_continuation(login_method, method='login')
print()

while True:
    valid_pass_mark = enter_value(value = "pass_mark")
    valid_defer_mark = enter_value(value = "defer_mark")
    valid_fail_mark = enter_value(value = "fail_mark")

    progress = get_progression_outcome(valid_pass_mark, valid_defer_mark, valid_fail_mark)
    print(progress + "\n")

    if progress == "Total incorrect.":
        continue
    elif valid_login_method == 's':
        break
    else:
        progressed_datalist.append([progress, valid_pass_mark, valid_defer_mark, valid_fail_mark])
        if progress == "Progress":
            progress_count = progress_count + 1
        elif progress == "Progress (module trailer)":
            trailer_count = trailer_count + 1
        elif progress == "Module retriever":
            retriever_count = retriever_count + 1
        else:
            exclude_count = exclude_count + 1

    print("Would you like to enter another set of data?")
    continue_result = input("Enter 'y' for yes or 'q' to quit and view results :")
    valid_continue_result = is_valid_continuation(continue_result, method='continue')
    print()

    if valid_continue_result=="y":
        continue
    elif valid_continue_result=="q":
        draw_histrogram(progress_count, trailer_count, retriever_count, exclude_count)
        display_data_list(progressed_datalist)
        break