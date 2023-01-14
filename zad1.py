import base64

x = input("Provide text to encode: ")
example_input = x
string_bytes = example_input.encode("ascii")

base64_bytes = base64.b64encode(string_bytes)
base64_string = base64_bytes.decode("ascii")

print(f"Encoded string: {base64_string}")
