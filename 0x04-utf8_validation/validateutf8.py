def validUTF8(data):
    num_bytes = 0

    for num in data:
        # Check the first byte
        if num < 0 or num > 255:
            return False  # Not a valid byte in UTF-8 range

        # Determine how many bytes this character should use
        if num_bytes == 0:
            if (num >> 7) == 0b0:
                num_bytes = 0  # 1-byte character
            elif (num >> 5) == 0b110:
                num_bytes = 1  # 2-byte character
            elif (num >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character
            elif (num >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid start byte
        else:
            # Check continuation byte
            if (num >> 6) != 0b10:
                return False  # Not a valid continuation byte
            num_bytes -= 1

    return num_bytes == 0  # All bytes must be accounted for

# Example usage
data = [197, 130, 1]  # Valid UTF-8
print(validUTF8(data))  # Output: True

data = [235, 140, 4]  # Invalid UTF-8
print(validUTF8(data))  # Output: False

