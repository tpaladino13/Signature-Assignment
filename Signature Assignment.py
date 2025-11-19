def get_average(marks):
    
    return sum(marks) / len(marks)


with open("grades.txt", "w") as file:
    for i in range(3):
        name = input("Enter student name: ")
        marks_input = input("Enter marks (comma-separated): ")

        
        marks = [float(m) for m in marks_input.split(",")]

        avg = get_average(marks)

      
        file.write(f"{name}: {avg:.2f}\n")


print("File contents:")
with open("grades.txt", "r") as file:
    for line in file:
        print(line.strip())
