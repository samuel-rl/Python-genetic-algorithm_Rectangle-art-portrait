<h1 align="center">Welcome to this Genetic algorithm 👋</h1>

We will try to recreate an image with rectangles.

The resulting images will be created in the folder `bestIndividus`.

<h2 align="center">Example</h2>

generation 0 :

![demo](https://github.com/samuel3105/Python-genetic-algorithm_Rectangle-art-portrait/blob/master/examples/gen0.png?raw=true)

generation 100 :

![demo](https://github.com/samuel3105/Python-genetic-algorithm_Rectangle-art-portrait/blob/master/examples/gen100.png?raw=true)

generation 600 :

![demo](https://github.com/samuel3105/Python-genetic-algorithm_Rectangle-art-portrait/blob/master/examples/gen600.png?raw=true)


<h2 align="center">Installation</h2>

```bash
# Clone the project :
git clone https://github.com/samuel3105/Python-genetic-algorithm_Rectangle-art-portrait.git
cd ./Python-genetic-algorithm_Rectangle-art-portrait

python3 imageGenetic.py
```

<h2 align="center">Documentation</h2>

Use args to change defaults settings

- `--N_RECTS` = int

    default = __50__
    
- `--CANVAS_SIZE` = int

    default = __100__
    
- `--POP_SIZE` = int

    default = __100__
    
- `--PROB_RECT_RESET` = float

    default = __0.01__
    
- `--INPUT_FILE` = string

    default = __"original.jpg"__
    

<h4>Example</h4>

```bash
python3 imageGenetic.py --N_RECTS 20 --INPUT_FILE myFile.jpg
```

```bash
python3 imageGenetic.py --CANVAS_SIZE 150 --INPUT_FILE myFile.jpg --POP_SIZE 150
```