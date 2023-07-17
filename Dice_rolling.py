
import random
  
DICE_ART= {
      1:("____________ ",
        "|           |",
        "|           |",
        "|     *     |",
        "|           |",
         "____________ "
      ),
      2:("____________ ",
        "|           |",
        "|  *        |",
        "|           |",
        "|        *  |",
         "____________ "
      ),
      3:("____________ ",
        "|           |",
        "|  *        |",
        "|     *     |",
        "|        *  |",
         "____________ "
      ),
      4:("____________ ",
        "|           |",
        "|  *     *  |",
        "|           |",
        "|  *     *  |",
         "____________ "
      ),
      5:("____________ ",
        "|           |",
        "|  *     *  |",
        "|     *     |",
        "|  *     *  |",
         "____________ "
      ),
      6:("____________ ",
        "|           |",
        "|  *     *  |",
        "|  *     *  |",
        "|  *     *  |",
         "____________ "
      ),
        
}
dice_height = len(DICE_ART[1])
dice_width = len(DICE_ART[1][0])
dice_face_separator="  "

def generate_dice_faces_diagram(dice_values):
      dice_faces=[]
      
      for values in dice_values:
            dice_faces.append(DICE_ART[values])
        
      dice_faces_rows=[]
      for row_idx in range(dice_height):
         row_components=[]
         for dice in dice_faces:
            row_components.append(dice[row_idx])
         row_string =dice_face_separator.join(row_components)
         dice_faces_rows.append(row_string)

      width=len(dice_faces_rows[0])
      diagram_header = "RESULTS".center(width,"-")
      dice_faces_diagram= "\n".join([diagram_header]+dice_faces_rows)
      return dice_faces_diagram

def parse_input(input_string):
        if input_string.strip() in {"1","2","3","4","5","6"}:
                return int(input_string)
        
        else:
                print("please enter a number from 1 to 6 ")
                raise SystemExit(1)

def roll_dice(num_dice):
    roll_result=[]
    for i in range(num_dice):
        roll=random.randint(1,6)
        roll_result.append(roll)
    return roll_result


        
# get the user input on number of dice rolling
num_dice_input = input("How many dice you want to roll ")
num_dice=parse_input(num_dice_input)
roll_results = roll_dice(num_dice)
dice_faces_diagram=generate_dice_faces_diagram(roll_results)
print(f"\n{dice_faces_diagram}")
