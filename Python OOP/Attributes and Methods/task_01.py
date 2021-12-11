class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        for sub_list in self.photos:
            if len(sub_list) < 4:
                sub_list.append(label)
                return f"{label} photo added successfully on page {self.photos.index(sub_list) + 1} " \
                       f"slot {sub_list.index(label) + 1}"

        return "No more free spots"

    def display(self):
        result = ""
        for sub_list in self.photos:
            result += "-" * 11 + "\n"
            result += " ".join(["[]" for sub in range(len(sub_list))]) + "\n"
        result += "-" * 11 + "\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


