import unittest
from homework_10 import log_event


class TestLogEvent(unittest.TestCase):

    def test_success_logs_info(self):
        with self.assertLogs("log_event", level="INFO") as log:
            log_event("Andrii", "success")

        self.assertIn("INFO:log_event:Login event - Username: Andrii, Status: success", log.output[0])
        print(log.output[0])
    def test_failure_logs_error(self):
        with self.assertLogs("log_event", level="ERROR") as log:
            log_event("Taras", "failure")

        self.assertIn("ERROR:log_event:Login event - Username: Taras, Status: failure", log.output[0])
        print(log.output[0])

    def test_warning_logs_warning(self):
        with self.assertLogs("log_event", level="WARNING") as log:
            log_event("Dima", "expired")

        self.assertIn("WARNING:log_event:Login event - Username: Dima, Status: expired", log.output[0])

        print(log.output[0])

if __name__ == "__main__":
    unittest.main()