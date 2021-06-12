from classes.video import Video

class Customer:
    #id,first_name,last_name,current_video_rentals
    def __init__(self, id, first_name, last_name, current_video_rentals=""):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    @classmethod
    def get_headers(self):
        #Called when saving data; Yes, if the file gets refactored, this will need to be as well.
        return ["id", "first_name", "last_name", "current_video_rentals"]

    def get_videos(self):
        # Convert videos to an array of strings, much easier to manipulate
        if self.current_video_rentals == "":
            # New customers start with no rentals
            return []
        else:
            # Customers from a file have their movie NAMES in an array of strings
            return self.current_video_rentals.split("/")

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
    
    def has_title(self, title):
        #Returns boolean if title already exists in Customer possession
        temp_array = self.get_videos()
        for v in temp_array:
            #Ignore case, because "of" and "the" are easy to mis-capitalize
            if v.lower() == title.lower():
                return True
        return False
    
    def get_id(self):
        return self.id

    def get_num_checkouts(self):
        return len(self.get_videos())
        
    def add_video(self, title):
        #Edge case if string is empty (otherwise they're charged for an empty movie they can't return, don't ask)
        if self.current_video_rentals == "":
            self.current_video_rentals = title
        self.current_video_rentals += "/" + title
        
    def remove_video(self, title):
        #Removes a video from self.current_video_rentals (string)
        # Annoying part is getting rid of the "/", so I'm converting to array to remove the element, then converting back to string

        #Convert my videos string to array
        temp_array = self.get_videos()
        for v in temp_array:
            #Ignore case, because "of" and "the" are easy to mis-capitalize
            if v.lower() == title.lower():
                temp_array.remove(v)
                #Convert my videos array to string
                self.current_video_rentals = "/".join(temp_array)
                return
        raise Exception(f"{self.first_name} {self.last_name} doesn't have {title}!")
