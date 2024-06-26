# For this exercise you will be strengthening your page-fu mastery. 
# You will complete the PaginationHelper class, which is a utility class helpful 
# for querying paging information related to an array.

# The class is designed to take in an array of values and an integer indicating 
# how many items will be allowed per each page. The types of values contained within 
# the collection/array are not relevant.

# The following are some examples of how this class is used:

# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count() # should == 2
# helper.item_count() # should == 6
# helper.page_item_count(0) # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid

# # page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid

# TODO: complete this class

class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        if not self.collection or self.items_per_page <= 0:
            return 0
        else:
            (len(self.collection) + self.items_per_page - 1) // self.items_per_page

    def page_item_count(self, page_index):
        if 0 <= page_index < self.page_count():
            return self.items_per_page if page_index < self.page_count() - 1 else len(self.collection) % self.items_per_page or self.items_per_page
        else:
            return -1  # Invalid page index

    def page_index(self, item_index):
        if item_index >= len(self.collection) or item_index < 0:
            return -1
        else:
            return item_index // self.items_per_page

        
helper = PaginationHelper([1,2,3,4], 4)
# print (helper.page_count()) # should == 2
# print (helper.item_count()) # should == 6
print (helper.page_item_count(0)) # should == 4
# print (helper.page_item_count(1)) # last page - should == 2
# print (helper.page_item_count(2))# should == -1 since the page is invalid
