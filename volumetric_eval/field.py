import numpy as np

class MaterialField:
    def __init__(self, dimensions: tuple = (50, 50, 50)):
        # Initialize a 3D grid representing material density (0.0 to 1.0)
        self.dimensions = dimensions
        self.density_grid = np.random.uniform(0.4, 1.0, size=dimensions)

    def get_local_resistance(self, position: tuple, sample_size: tuple) -> float:
        x, y, z = position
        sx, sy, sz = sample_size
        region = self.density_grid[x:x+sx, y:y+sy, z:z+sz]
        if region.size == 0:
            return 1.0
        return float(np.mean(region))
