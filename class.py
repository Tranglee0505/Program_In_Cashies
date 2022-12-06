# class Video:
#     def __init__(self,title,link):
#         self.title = title
#         self.link = link

# def read_video():
#     title = input("Enter title :")
#     link = input("Enter link :")
#     video = Video(title,link)

# def read_videos():
#     videos = []
#     total_video = int(input("Enter how many video :"))
#     for i in range(total_video):
#         print(" Enter video", i+1)
#         vid = read_video()
#         videos.append(vid)

# def print_video(video):
#     print("Video title :", video.title)
#     print("Video link :", video.link)

# def main():
#     total_video = int(input("Enter how many videos:"))
#     vid = read_video()
#     print_video(vid)

# main()


p = float(input('Số tiền gốc ban đầu: '))
t = float(input('Số năm cho vay: '))
r = float(input('Lãi suất danh nghĩa hàng năm: '))
n = float(input('Số lần ghép lãi trong một năm: '))
a = p*(1+(r/n))**(n*t)
print('Tổng số tiền là: ', a)