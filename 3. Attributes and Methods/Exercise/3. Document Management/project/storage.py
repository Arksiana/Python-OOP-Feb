class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [c for c in self.categories if c.id == category_id][0]
        if category:
            category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [c for c in self.topics if c.id == topic_id][0]
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = [c for c in self.documents if c.id == document_id][0]
        if document:
            document.file_name = new_file_name

    def delete_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id][0]
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [c for c in self.topics if c.id == topic_id][0]
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [c for c in self.documents if c.id == document_id][0]
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        document = [c for c in self.documents if c.id == document_id][0]
        if document:
            return document

    def __repr__(self):
        result = ''
        for document in self.documents:
            result += f"{document.__repr__()}\n"
        return result
