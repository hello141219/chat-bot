import unittest
from ai_chat.chatbot import ChatBot

class TestChatBot(unittest.TestCase):
    def test_get_response(self):
        bot = ChatBot()
        response = bot.get_response("Hello")
        self.assertEqual(response, "This is a placeholder response.")

if __name__ == "__main__":
    unittest.main() 