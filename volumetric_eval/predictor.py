from typing import List, Dict
from .tools import VolumetricTool
from .field import MaterialField

class CarvingPredictor:
    def __init__(self, field: MaterialField, energy_budget: float):
        self.field = field
        self.energy_budget = energy_budget

    def evaluate_trajectory(self, tool: VolumetricTool, trajectory: List[tuple]) -> Dict:
        total_energy = 0.0
        instability_index = 0.0
        voxels_carved = 0

        for pos in trajectory:
            resistance = self.field.get_local_resistance(pos, tool.kernel_shape)
            step_voxels = tool.kernel_shape[0] * tool.kernel_shape[1] * tool.kernel_shape[2]
            
            # Energy cost scales with local material resistance
            step_cost = step_voxels * tool.energy_per_voxel * resistance
            total_energy += step_cost
            voxels_carved += step_voxels

            # Heuristic for structural instability based on dense clusters being hollowed out
            if resistance > 0.8:
                instability_index += 0.08

        feasible = total_energy <= self.energy_budget and instability_index < 0.7

        return {
            "tool": tool.name,
            "feasible": feasible,
            "projected_energy_cost": round(total_energy, 2),
            "voxels_extracted": voxels_carved,
            "structural_risk": round(instability_index, 3)
        }
