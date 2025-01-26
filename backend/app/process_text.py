# Built-in imports
from datetime import datetime

# Own imports
from common.logger import custom_logger

from app.bedrock_agent import call_bedrock_agent


logger = custom_logger()


class ProcessText:
    """
    This class contains methods that serve as the "text processing" for the State Machine.
    """

    def __init__(self, event, session_id):
        self.logger = logger
        self.event = event
        self.session_id = session_id

    def process_text(self):
        """
        Method to validate the input message and process the expected text response.
        """

        self.logger.info("Starting process_text for the multi-agent demo")

        # TODO: Add more robust "text processing" logic here (actual response)
        self.text = self.event.get("input")

        # TODO: Add more complex "text processing" logic here with memory and sessions...
        self.response_message = call_bedrock_agent(self.text, self.session_id)

        self.logger.info(f"Generated response message: {self.response_message}")
        self.logger.info("Validation finished successfully")

        self.event["response_message"] = self.response_message

        return self.event


if __name__ == "__main__":
    event = {
        "input": "What are my products?",
        "messageVersion": "1.0",
        "session_id": "SantiTests",  # Intentionally hard-coded for local tests
    }

    process_text = ProcessText(
        event,
    )
    process_text.process_text()
    print(process_text.response_message)
