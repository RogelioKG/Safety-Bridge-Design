def main():
    import os
    current_dir_name = os.path.basename(os.path.dirname(__file__))
    test_file_name = input("test file name: ")
    assert "&" not in test_file_name
    os.system(f"cd.. & py -m {current_dir_name}.tests.{test_file_name}")


if __name__ == "__main__":
    main()
