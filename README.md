# self-organising-map
A codebase to explore a self organising map to visualize high dimension data as an image.

## Requirements
- Docker
- Python3.11
- Poetry (Optional)

## Usage
### With CLI prompts
`python3 kohonen/main.py`

### Without CLI prompts
`python3 kohonen/main.py --map_size 3 3 --input_vector_size 4`

### Build image
`make build-base`

### Run Tests
`make build-test`
