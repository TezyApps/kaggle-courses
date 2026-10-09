import sys
import tensorflow as tf

def __print_title(text: str):
    print(f"[{text}]")
    print("-" * (len(text) + 4))

def check_tensorflow():
    __print_title("Checking Tensorflow...")
    print(f"Tensorflow Version : {tf.__version__}")
    print(f"Tensorflow Devices: {tf.config.list_physical_devices()}")
    print("\n")

def check_python():
    __print_title("Checking Python...")
    print(sys.version)
    print(sys.executable)
    print("\n")

if __name__ == '__main__':
    check_python()
    check_tensorflow()
