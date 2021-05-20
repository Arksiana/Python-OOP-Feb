from abc import ABC, abstractmethod


# Single responsibility, Liskov, open-closed, dependency injection

class IContent(ABC):
    @abstractmethod
    def format(self, format, content=None, available_formats={}):
        pass


class HTMLFormatter(IContent):
    def format(self, content):
        return f"<h1>{content}</h1>"


class MyMLFormatter(IContent):
    def format(self, content):
        return '\n'.join(['<myML>', content, '</myML>'])


class BasicFormatter(IContent):
    def format(self, content):
        return content.capitalize()


class Email:
    def __init__(self, content, formatter):
        self.content = formatter().format(content)


email = Email('ads', MyMLFormatter)
print(email.content)
