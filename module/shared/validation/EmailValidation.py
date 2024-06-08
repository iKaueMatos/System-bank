import re


class EmailValidation:

      @staticmethod
      def is_valid_email(self, email):
            pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            return re.match(pattern, email) is not None