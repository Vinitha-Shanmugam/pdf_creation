import msgpack


def read_msgpack_file(file_path):
    with open(file_path, 'rb') as file:
        packed_data = file.read()
        data = msgpack.unpackb(packed_data, raw=False)  # Use raw=False for string decoding
    return data


if __name__ == "__main__":
    msgpack_file_path = r"C:\Users\Vrdella\Documents\PDF\output_texts.msgpack"

    try:
        unpacked_data = read_msgpack_file(msgpack_file_path)
        for filename, text in unpacked_data.items():
            print(f"Filename: {filename}")
            print("Text:")
            print(text)
            print("\n" + "=" * 30 + "\n")
    except Exception as e:
        print(f"Error reading MessagePack file: {e}")
