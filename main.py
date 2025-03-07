from capture_faces import capImg
from train_Model import train
from recognise_face import recog
from attendance import viewAtt

def main():
    while True:
        print("\n1. Capture Face\n2. Train Model\n3. Recognize Faces\n4. View Attendance\n5. Exit")
        choice = input("> ")

        if choice == "1":
            capImg(input("Enter name: "))
        elif choice == "2":
            train()
        elif choice == "3":
            recog()
        elif choice == "4":
            viewAtt()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
