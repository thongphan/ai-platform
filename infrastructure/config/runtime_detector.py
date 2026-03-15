import os


class RuntimeDetector:

    @staticmethod
    def detect():

        try:
            import google.colab
            return "colab"
        except ImportError:
            pass

        if os.getenv("GITHUB_ACTIONS"):
            return "ci"

        return None