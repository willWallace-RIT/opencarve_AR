import numpy as np

class VolumetricTool:
    def __init__(self, name: str, kernel_shape: tuple, energy_per_voxel: float, material_bias: str = "generic"):
        self.name = name
        self.kernel_shape = kernel_shape  # (depth, width, height) 3D footprint
        self.energy_per_voxel = energy_per_voxel
        self.material_bias = material_bias

    def carve(self, density_field: np.ndarray, position: tuple) -> np.ndarray:
        """
        Applies the tool's geometric footprint to a target spatial field,
        simulating volumetric destruction.
        """
        x, y, z = position
        kx, ky, kz = self.kernel_shape
        
        # Ensure bounds don't exceed the field dimensions
        max_x, max_y, max_z = density_field.shape
        end_x = min(x + kx, max_x)
        end_y = min(y + ky, max_y)
        end_z = min(z + kz, max_z)

        # Modify material density in the target region
        sub_region = density_field[x:end_x, y:end_y, z:end_z]
        carved_region = sub_region * 0.1  # Residual material left behind
        density_field[x:end_x, y:end_y, z:end_z] = carved_region
        
        return density_field
