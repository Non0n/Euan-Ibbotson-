import matplotlib.pyplot as plt
import numpy as np
#importing the needed libraries 
   
Teams1 = []
Points1 = []

Teams2 = ['Liverpool', 'Man City', 'Man United', 'Chelsea', 'Leicester', 'Tottenham', 'Wolves', 'Arsenal', 'Sheffield', 'Burnley', 'Southampton', 'Everton', 'Newcastle', 'Crystal Palace', 'Brighton', 'West Ham', 'Aston Villa', 'Bournemouth', 'Watford', 'Norwich City']
Points2 = [99, 81, 66, 66, 62, 59, 59, 56, 54, 54, 52, 49, 44, 43, 41, 39, 35, 34, 34, 21]

Teams3 = []
Points3 = []
#Declaring all of the teams and the points that they recieved in that season

def menu():
    print("Please choose what season you would like to view:")
    print("[1] 2018/19")
    print("[2] 2019/20")
    print("[3] 2020/21")


menu()
option1 = int(input("Please enter your option: "))

while option1 != 0:
    if option1 == 1:
        print("Premier League Table 2019/20")
        print("Please choose what type of data visualisation you would like to see:")
        print("[1] Bar Chart")
        print("[2] Pie Chart")
        print("[0] Exit the program.")
        # Text based menu thats allows the user to input an option
      
        
        option2 = int(input("Please enter your option: "))

        while option2 != 0:
            if option2 == 1:
            # This option will display a visualisation of a bar chart
                plt.bar(Teams1, Points1)
                plt.title('Premier League Table 2019/20 Season')
                plt.xlabel('Teams1')
                plt.ylabel('Points1')
                plt.show()
               
            elif option2 == 2:
            # his option will display a visualisation of a pie chart which displays the distribution of all points in the premier league table
                fig1 = plt.figure()
                ax1 = fig1.add_axes([0,0,1,1])
                ax1.axis('equal')
                ax1.pie(Points1, labels1 = Teams1,autopct='%.2f%%')
                plt.show()
            else:
                print("Invalid option, please try again.")

        print()        
        option2 = int(input("Please enter your option: "))

    elif option1 == 2:
        
        print("Premier League Table 2019/20")
        print("Please choose what type of data visualisation you would like to see:")
        print("[1] Bar Chart")
        print("[2] Pie Chart")
        print("[0] Exit the program.")
        # Text based menu thats allows the user to input an option
      
        
        option3 = int(input("Please enter your option: "))

        while option3 != 0:
            if option3 == 1:
            # This option will display a visualisation of a bar chart
                plt.bar(Teams2, Points2)
                plt.title('Premier League Table 2019/20 Season')
                plt.xlabel('Teams2')
                plt.ylabel('Points2')
                plt.show()
               
            elif option3 == 2:
            # his option will display a visualisation of a pie chart which displays the distribution of all points in the premier league table
                fig2 = plt.figure()
                ax2 = fig2.add_axes([0,0,1,1])
                ax2.axis('equal')
                ax2.pie(Points2, labels2 = Teams2,autopct='%.2f%%')
                plt.show()
            else:
                print("Invalid option, please try again.")

        print()        
        option3 = int(input("Please enter your option: "))
    
    elif option1 == 3:
        print("Premier League Table 2019/20")
        print("Please choose what type of data visualisation you would like to see:")
        print("[1] Bar Chart")
        print("[2] Pie Chart")
        print("[0] Exit the program.")
        # Text based menu thats allows the user to input an option
      
        
        option4 = int(input("Please enter your option: "))

        while option4 != 0:
            if option4 == 1:
            # This option will display a visualisation of a bar chart
                plt.bar(Teams3, Points3)
                plt.title('Premier League Table 2019/20 Season')
                plt.xlabel('Teams3')
                plt.ylabel('Points3')
                plt.show()
               
            elif option4 == 2:
            # his option will display a visualisation of a pie chart which displays the distribution of all points in the premier league table
                fig3 = plt.figure()
                ax3 = fig3.add_axes([0,0,1,1])
                ax3.axis('equal')
                ax3.pie(Points3, labels3 = Teams3,autopct='%.2f%%')
                plt.show()
            else:
                print("Invalid option, please try again.")

        print()        
        option4 = int(input("Please enter your option: "))

    else:
        print("Invalid option, please try again.")

    print()
    menu()
    option1 = int(input("Please enter your option: "))




print("Thank you, goodbye.")
