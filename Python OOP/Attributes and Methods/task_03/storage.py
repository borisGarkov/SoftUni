from task_03.category import Category
from task_03.document import Document
from task_03.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        return "\n".join([document.__repr__() for document in self.documents])

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        filtered_category = [category for category in self.categories if category.id == category_id]
        if filtered_category:
            category = filtered_category[0]
            category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        filtered_topic = [topic for topic in self.topics if topic.id == topic_id]
        if filtered_topic:
            topic = filtered_topic[0]
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        filtered_document = [document for document in self.documents if document.id == document_id]
        if filtered_document:
            document = filtered_document[0]
            document.file_name = new_file_name

    def delete_category(self, category_id):
        filtered_category = [category for category in self.categories if category.id == category_id]
        if filtered_category:
            self.categories.remove(filtered_category[0])

    def delete_topic(self, topic_id):
        filtered_topic = [topic for topic in self.topics if topic.id == topic_id]
        if filtered_topic:
            self.topics.remove(filtered_topic[0])

    def delete_document(self, document_id):
        filtered_document = [document for document in self.documents if document.id == document_id]
        if filtered_document:
            self.documents.remove(filtered_document[0])

    def get_document(self, document_id):
        filtered_document = [document for document in self.documents if document.id == document_id]
        if filtered_document:
            return filtered_document[0]
