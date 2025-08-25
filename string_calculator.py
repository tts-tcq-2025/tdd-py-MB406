"""
StringCalculator implementation using TDD approach
Following principles of modularity, refactoring, and future usability
"""


class StringCalculator:
    """A calculator that can add numbers from string inputs with various delimiters."""
    
    def __init__(self):
        """Initialize the StringCalculator with default delimiters."""
        self.default_delimiters = [',', '\n']
    
    def add(self, numbers):
        """
        Add numbers from a string input.
        
        Args:
            numbers (str): String containing numbers to add
            
        Returns:
            int: Sum of the numbers
        """
        if numbers == "":
            return 0
        
        # Parse numbers from the string
        number_list = self._parse_numbers(numbers)
        
        # Calculate and return the sum
        return sum(number_list)
    
    def _parse_numbers(self, numbers):
        """
        Parse numbers from the input string using appropriate delimiters.
        
        Args:
            numbers (str): String containing numbers to parse
            
        Returns:
            list: List of integers parsed from the string
        """
        # Check for custom delimiter format
        custom_delimiter, number_string = self._extract_custom_delimiter(numbers)
        
        # Get all delimiters to use
        delimiters = self.default_delimiters.copy()
        if custom_delimiter:
            delimiters.append(custom_delimiter)
        
        # Replace all delimiters with a common delimiter
        normalized_numbers = self._normalize_delimiters(number_string, delimiters)
        
        # Split by the common delimiter and convert to integers
        number_list = [int(num.strip()) for num in normalized_numbers.split(',') if num.strip()]
        
        # Validate no negative numbers
        self._validate_no_negatives(number_list)
        
        # Filter out numbers bigger than 1000
        filtered_numbers = self._filter_large_numbers(number_list)
        
        return filtered_numbers
    
    def _extract_custom_delimiter(self, numbers):
        """
        Extract custom delimiter if present in the format //[delimiter]\n or //delimiter\n
        
        Args:
            numbers (str): Input string that may contain custom delimiter
            
        Returns:
            tuple: (custom_delimiter, number_string) or (None, original_string)
        """
        if numbers.startswith('//'):
            lines = numbers.split('\n', 1)
            if len(lines) == 2:
                delimiter_line = lines[0][2:]  # Remove '//'
                number_string = lines[1]
                
                # Check if delimiter is in brackets format //[delimiter]\n
                if delimiter_line.startswith('[') and delimiter_line.endswith(']'):
                    delimiter = delimiter_line[1:-1]  # Remove brackets
                    return delimiter, number_string
                else:
                    # Simple format //delimiter\n
                    return delimiter_line, number_string
        
        return None, numbers
    
    def _normalize_delimiters(self, numbers, delimiters=None):
        """
        Replace all delimiters with commas for consistent parsing.
        
        Args:
            numbers (str): String with various delimiters
            delimiters (list): List of delimiters to normalize
            
        Returns:
            str: String with normalized delimiters (commas only)
        """
        if delimiters is None:
            delimiters = self.default_delimiters
            
        normalized = numbers
        for delimiter in delimiters:
            if delimiter != ',':  # Don't replace commas with commas
                normalized = normalized.replace(delimiter, ',')
        return normalized
    
    def _validate_no_negatives(self, number_list):
        """
        Validate that no negative numbers are present in the list.
        
        Args:
            number_list (list): List of integers to validate
            
        Raises:
            ValueError: If negative numbers are found
        """
        negatives = [num for num in number_list if num < 0]
        if negatives:
            negative_str = ', '.join(str(num) for num in negatives)
            raise ValueError(f"negatives not allowed: {negative_str}")
    
    def _filter_large_numbers(self, number_list, max_value=1000):
        """
        Filter out numbers bigger than max_value.
        
        Args:
            number_list (list): List of integers to filter
            max_value (int): Maximum allowed value (default: 1000)
            
        Returns:
            list: Filtered list with numbers <= max_value
        """
        return [num for num in number_list if num <= max_value]
