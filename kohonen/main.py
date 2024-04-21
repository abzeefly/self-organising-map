import argparse
from matplotlib import pyplot as plt
from src.kohonen import Network, InputVector, KohonenTrainer


def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Kohonen Network")

    # Add arguments
    parser.add_argument(
        "--map_size",
        type=int,
        nargs=2,
        help="Tuple with length 2 representing the size of the map (e.g., '3 3' for a 3x3 map)",
    )
    parser.add_argument("--input_vector_size", type=int, help="Size of the input vector")

    # Parse the arguments
    args = parser.parse_args()

    # Ask for map size if not providedß
    if args.map_size is None:
        map_size = tuple(map(int, input("Enter map size (e.g., '3 3' for a 3x3 map): ").split()))
    else:
        map_size = tuple(args.map_size)
    
    # Ask for input vector size if not provided
    if args.input_vector_size is None:
        input_vector_size = int(input("Enter input vector size: "))
    else:
        input_vector_size = args.input_vector_size

    # Extract map size and input vector size from arguments
    map_size = map_size
    input_vector_size = input_vector_size

    # Create the input vector
    input_vector = InputVector(size=input_vector_size)
    # Create the network
    network = Network(map_size=map_size, input_vector_size=input_vector.size)
    # Create Kohonen Training
    kohonen_training = KohonenTrainer(network=network, input_vector=input_vector, max_iterations=100)
    # Run Kohonen Training
    kohonen_training.train()

    # Get data to produce image
    image_data = network.get_image_data()

    # Save image locally
    plt.imshow(image_data)
    plt.savefig("output.png")


if __name__ == "__main__":
    main()
