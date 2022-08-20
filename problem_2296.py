"""
Design a text editor with a cursor that can do the following:

Add text to where the cursor is.
Delete text from where the cursor is (simulating the backspace key).
Move the cursor either left or right.
When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.

Implement the TextEditor class:

TextEditor() Initializes the object with empty text.
void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.
int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the
cursor, where len is the number of characters to the left of the cursor.
string cursorRight(int k) Moves the cursor to the right k times.
Returns the last min(10, len) characters to the left of the cursor,
where len is the number of characters to the left of the cursor.
"""

test_input1 = ["TextEditor", "addText", "deleteText", "addText", "cursorRight",
              "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
test_input2 = [[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
test_output = [None, None, 4, None, "etpractice", "leet", 4, "", "practi"]


class DoubleLinkedList(object):

    def __init__(self, key, next=None, previous=None):
        self.key = key
        self.next = next
        self.previous = previous


def return_last(current):
    i = 10
    last_char = ''
    while i and current:
        last_char += current.key
        current = current.previous
        i -= 1
    return last_char[::-1]


class TextEditor(object):

    def __init__(self):
        self.cursor = DoubleLinkedList("|")

    def addText(self, text):
        """Add input text to right of cursor"""
        previous = self.cursor.previous
        for char in text:
            current = DoubleLinkedList(char, previous=previous)
            if previous:
                previous.next = current
            previous = current
        self.cursor.previous = current

    def deleteText(self, k):
        """Delete up to k chars to left of cursor and return num of chars deleted"""
        current = self.cursor.previous
        i = k
        while i and current:
            next = current.previous
            del current
            current = next
            i -= 1
        self.cursor.previous = current
        return k - i

    def cursorLeft(self, k):
        """Move cursor left k places and return max 10 chars to left of cursor"""
        current = self.cursor.previous
        if current:
            current.next = self.cursor.next
            while k and current:
                k -= 1
                previous = current
                current = current.previous
            self.cursor.previous = previous.previous
            self.cursor.next = previous
            if previous.previous:
                previous.previous.next = self.cursor
            previous.previous = self.cursor
        current = self.cursor.previous
        return return_last(current)

    def cursorRight(self, k):
        """Move cursor right k places and return max 10 chars to left of cursor"""
        current = self.cursor.next
        if current:
            current.previous = self.cursor.previous
            if current.previous:
                current.previous.next = current
            while k and current:
                k -= 1
                previous = current
                current = current.next
            self.cursor.previous = previous
            self.cursor.next = previous.next
            if previous.next:
                previous.next.previous = self.cursor
            previous.next = self.cursor
        current = self.cursor.previous
        return return_last(current)

    def __str__(self):
        text = ''
        current = self.cursor.previous
        while current:
            text += current.key
            current = current.previous
        text = text[::-1]
        text += self.cursor.key
        current = self.cursor.next
        while current:
            text += current.key
            current = current.next
        return text


def test():
    text_editor = TextEditor()
    for input1, input2, output1 in zip(test_input1[1:], test_input2[1:], test_output[1:]):
        if input1 == 'addText':
            assert text_editor.addText(input2[0]) == output1
        elif input1 == 'deleteText':
            assert text_editor.deleteText(input2[0]) == output1
        elif input1 == 'cursorLeft':
            assert text_editor.cursorLeft(input2[0]) == output1
        elif input1 == 'cursorRight':
            assert text_editor.cursorRight(input2[0]) == output1


test()
