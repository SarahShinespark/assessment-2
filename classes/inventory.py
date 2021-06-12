from classes.video import Video
import csv, os.path

#Holds the Video files in a list and handles file I/O
class Inventory:
    def __init__(self, source_file):
        #Remind me to make sure my __str__ methods RETURN STRINGS *before* adding a try-except block
        try:
            self.videos = self.populate_videos(source_file)
            # print("I got the videos.")
        except Exception as e:
            print("Inventory retrieval failed, error", e)
            self.videos = []

    def __str__(self):
        #Print a list of all videos with print(self)
        output = ""
        for i, video in enumerate(self.videos):
            output += str(video)
            if i != len(self.videos)-1:
                output += "\n"
        return output
        
    @classmethod
    def populate_videos(cls, source_file):
        #Initializes the Video list
        videos = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        my_path += "/../data"
        path = os.path.join(my_path, source_file)

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                videos.append(Video(**dict(row)))
        return videos
    
    def persist_inventory(self, source_file):
        #Saves the Video list to a file
        my_path = os.path.abspath(os.path.dirname(__file__))
        my_path += "/../data"
        path = os.path.join(my_path, source_file)

        with open(path, "w") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=Video.get_headers())
            writer.writeheader()
            for video in self.videos:
                writer.writerow(video.__dict__)

    def get_video_from_title(self, title):
        # Search Inventory for title. I convert to lowercase because it's easy to miss capital "The" in titles
        for v in self.videos:
            if v.get_title().lower() == title.lower():
                return v
        raise Exception("Couldn't find video title.")
