import json
def load_video():
    try:
        with open("data.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_video_helper(videos):
    with open('data.txt',"w") as file:
       
       json.dump(videos,file)

def List_all_videos(videos):
    for index,video in enumerate(videos, start=1):
        print("index",index)

def Add_new_video(videos):
    name=input("Enter video name")
    time=input("Enter video time")
    videos.append({"name":name,"time":time})
    save_video_helper(videos)
def Update_video(videos):
    pass
def Delete_video(videos):
    pass


def main():
    videos=load_video()
    while True:
        print("\n Youtube Manager|choose an option")
        print("1 list all youtube videos")
        print("2 add new youtube video")
        print("3 update youtube video")
        print("4 Delete youtube video")
        print("5 Exit the app")
        choice=input("Enter your choice")
        print(videos)

        match choice:
            case "1":
                List_all_videos(videos)
            case "2":
                Add_new_video(videos)

            case "3":
                Update_video(video)
            case "4":
                Delete_video(video)
            case "5":
                break
            case _:
                print("invalid choice")

if __name__=="__main__":
    main()