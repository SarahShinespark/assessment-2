#Holds video information
#These are the records stored in <inventory.csv>
#Mostly this class contains helper methods to assist displaying the data.
class Video:
    def __init__(self,id,title,rating,copies_available=0):
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = int(copies_available)

    def __str__(self):
        return f"ID {self.id}, {self.title} is rated {self.rating}. We have {self.copies_available} in stock."
        
    def get_title(self):
        return self.title
        
    def get_copies(self):
        return self.copies_available