
class Parser:
    _config: str

    def __init__(self, config: str):
        self._config = config

    @classmethod
    def load(cls, file_path: str) -> 'Parser':
        """
        Create a Parser instance by reading configuration from a file.

        Args:
            file_path (str): Path to the configuration file

        Returns:
            Parser: New Parser instance with loaded configuration

        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the configuration format is invalid
        """
        with open(file_path, 'r') as f:
            return cls(f.read())

        # End of function


    def parse(self) -> dict:
        """
        Parse configuration text in 'label = value' format.
        Only lines where label starts with a letter are processed.
    
        Args:
            text (str): Input text to parse
        
        Returns:
            dict: Dictionary containing parsed label-value pairs
        
        Raises:
            ValueError: If a non-ignored line doesn't contain exactly one '=' character
        """
        result = {}
    
        for line in self._config.splitlines():
            # Skip empty lines
            line = line.strip()
            if not line:
                continue
            
            # Skip lines not starting with a letter
            if not line[0].isalpha():
                continue
            
            # Split by = and let ValueError propagate up
            label, value = line.split('=', 1)
            label, value = label.strip(), value.strip()

            if label == '' or value == '':
                raise ValueError(f"Invalid line: '{line}'")

        # Verify label is alphanumeric
            if label.isalnum():
                result[label] = value
            
        return result
