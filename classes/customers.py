from classes.video import Video

class Customer:
    #id,first_name,last_name,current_video_rentals
    def __init__(self, id, first_name, last_name, current_video_rentals=""):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        # Convert videos to an array of strings, much easier to manipulate
        if current_video_rentals == "":
            # New customers start with no rentals
            self.video_names = []
        else:
            # Customers from a file have their movie NAMES in an array of strings
            self.video_names = self.parse_video_string(current_video_rentals)
        
    def parse_video_string(self, vid_string):
        return vid_string.split("/")
        
    def __str__(self):
        #Print the customer's info
        output = f"{self.first_name} {self.last_name} has checked out: "
        if len(self.video_names) == 0:
            return output + "NO VIDEOS."
        for i, name in enumerate(self.video_names):
            output += name
            if i != len(self.video_names)-1:
                output += ", "
            else:
                output += "."
        return output

    def get_id(self):
        return self.id

    def get_videos(self):
        return self.video_names
        
    def get_num_checkouts(self):
        return len(self.video_names)
        
    def add_video(self, title):
        self.video_names.append(title)
        
    def remove_video(self, title):
        for v in self.video_names:
            if v.lower() == title.lower():
                self.video_names.remove(v)
                return
        raise Exception(f"{self.first_name} {self.last_name} doesn't have {title}!")