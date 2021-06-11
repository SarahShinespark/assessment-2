from classes.video import Video

class Customer:
    #id,first_name,last_name,current_video_rentals
    def __init__(self, id, first_name, last_name, current_video_rentals=""):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    def get_videos(self):
        # Convert videos to an array of strings, much easier to manipulate
        if self.current_video_rentals == "":
            # New customers start with no rentals
            return []
        else:
            # Customers from a file have their movie NAMES in an array of strings
            return self.current_video_rentals.split("/")

    # @classmethod
    # def parse_video_string(cls, vid_string):
    #     # Converts "Movie1/Movie2/Movie3" -> ["Movie1","Movie2","Movie3"]
    #     return vid_string.split("/")

    # def get_stringified_videos(self):
    #     # Converts ["Movie1","Movie2","Movie3"] -> "Movie1/Movie2/Movie3"
    #     return "/".join(self.video_names)
        
    def __str__(self):
        #Print the customer's info
        output = f"{self.first_name} {self.last_name} has checked out: "
        if len(self.current_video_rentals) == 0:
            return output + "NO VIDEOS."
        rental_array = self.get_videos()
        for i, name in enumerate(rental_array):
            output += name
            if i != len(rental_array)-1:
                output += ", "
            else:
                output += "."
        return output

    def get_id(self):
        return self.id

    def get_num_checkouts(self):
        return len(self.get_videos())
        
    def add_video(self, title):
        self.current_video_rentals += "/" + title
        
    def remove_video(self, title):
        for v in self.get_videos():
            if v.lower() == title.lower():
                self.video_names.remove(v)
                return
        raise Exception(f"{self.first_name} {self.last_name} doesn't have {title}!")