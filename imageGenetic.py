import random
from PIL import Image
from sys import argv
from classes.color import Color

N_RECTS = 40
CANVAS_SIZE = 125
POP_SIZE = 150
PROB_RECT_RESET = 0.00

def drawIndividu(individu):
    canvas = [[[0,0,0] for x in range(CANVAS_SIZE)] for y in range(CANVAS_SIZE)]
    for x,y,w,h,color,a in individu.rects:
        for xx in range(x, x+w):
            if not 0<=xx<CANVAS_SIZE:
                continue
            for yy in range(y, y+h):
                if not 0<=yy<CANVAS_SIZE:
                    continue
                newpixel = []
                for i in range(3):
                    newcomponent = int((1-a) * color[i] + a * canvas[yy][xx][i])
                    newpixel.append(newcomponent)
                canvas[yy][xx] = newpixel
    return canvas

def saveCanvas(canvas, filename):
    res = []
    for r in canvas:
        res.extend(map(tuple, r))
    im = Image.new('RGB', (CANVAS_SIZE, CANVAS_SIZE))
    im.putdata(res)
    im.save(filename)

def saveDoubleCanvas(canvas1, canvas2, filename):
    res = []
    for r in canvas1:
        res.extend(map(tuple, r))
    im1 = Image.new('RGB', (CANVAS_SIZE, CANVAS_SIZE))
    im1.putdata(res)

    res = []
    for r in canvas2:
        res.extend(map(tuple, r))
    im2 = Image.new('RGB', (CANVAS_SIZE, CANVAS_SIZE))
    im2.putdata(res)

    im = Image.new('RGB', (CANVAS_SIZE * 2, CANVAS_SIZE))
    im.paste(im1, (0,0))
    im.paste(im2, (CANVAS_SIZE, 0))
    im.save(filename)

def calcFitness(individu, final):
    canvasIndividu = drawIndividu(individu)
    fit = 0;
    for x in range(CANVAS_SIZE):
        for y in range(CANVAS_SIZE):
            for c in range(3):
                fit += (canvasIndividu[x][y][c] - final[x][y][c]) ** 2
    return fit

def reproductionIndiv(indivg, indivd):
    poidsGauche = random.randrange(N_RECTS)
    enfant = indivg.rects[:poidsGauche] + indivd.rects[poidsGauche:]
    return Individu(enfant)

def mutationIndiv(indiv):
    for i in range(N_RECTS):
        if random.random() < PROB_RECT_RESET:   
            #w = int(random.betavariate(2,5) * CANVAS_SIZE)
            #h = int(random.betavariate(2,5) * CANVAS_SIZE)
            w = int(random.betavariate(1,2) * CANVAS_SIZE//2)
            h = int(random.betavariate(1,2) * CANVAS_SIZE//2)
            x = random.randrange(CANVAS_SIZE - w)
            y = random.randrange(CANVAS_SIZE - h)
            c = random.randrange(255)
            a = random.random()
            indiv.rects[i] = (x,y,w,h,(c,c,c),a)

class Individu(object):
    def __init__(self, rects=None):
        if rects is not None:
            assert len(rects) == N_RECTS
            self.rects = rects
            return
        self.rects = []
        for _ in range(N_RECTS):
            w = int(random.betavariate(2,5) * CANVAS_SIZE)
            h = int(random.betavariate(2,5) * CANVAS_SIZE)
            x = random.randrange(CANVAS_SIZE - w)
            y = random.randrange(CANVAS_SIZE - h)
            c = random.randrange(255)
            a = random.random()
            self.rects.append((x,y,w,h,(c,c,c),a))


if __name__ == "__main__":


    image = Image.open('original3.jpg').convert('L').convert('RGB').resize((CANVAS_SIZE, CANVAS_SIZE))
    imagePix = image.load()
    imageCanvas = [[imagePix[x,y] for x in range(CANVAS_SIZE)] for y in range(CANVAS_SIZE)]

    population = []

    for _ in range(POP_SIZE):
        population.append(Individu())

    for generation in range(1000):
        print('GENERATION', Color.GREEN,generation, Color.END)
        popFitness = []
        for individu in population:
            popFitness.append((calcFitness(individu, imageCanvas), random.random(), individu))
        popFitness.sort()
        popFitness = popFitness[:POP_SIZE // 2]
        bestIndiv = min(zip(popFitness, population))[1]
        saveDoubleCanvas(imageCanvas, drawIndividu(bestIndiv), f'bestIndivs/gen{generation}.png')
        #saveCanvas(drawIndividu(bestIndiv), f'bestIndivs/gen{generation}.png')
        population = [popf[2] for popf in popFitness]
        enfants = []
        while len(enfants) + len(population) < POP_SIZE:
            parent1, parent2 = random.sample(population, 2)
            enfant = reproductionIndiv(parent1, parent2)
            enfants.append(enfant)
            
        population.extend(enfants)

        for i in range(POP_SIZE):
            mutationIndiv(population[i])