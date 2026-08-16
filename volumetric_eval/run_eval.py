from volumetric_eval.field import MaterialField
from volumetric_eval.tools import VolumetricTool
from volumetric_eval.predictor import CarvingPredictor

def main():
    print("Initializing Isolated Material Field...")
    field = MaterialField(dimensions=(30, 30, 30))
    
    predictor = CarvingPredictor(field, energy_budget=100.0)

    # Define different tool archetypes (Geo-Mod style volumetric footprints)
    point_drill = VolumetricTool("High-Frequency Point Drill", kernel_shape=(1, 1, 3), energy_per_voxel=0.5)
    linear_cutter = VolumetricTool("Thermal Line Cutter", kernel_shape=(2, 2, 1), energy_per_voxel=1.2)
    explosive_charge = VolumetricTool("Shaped Explosive Charge", kernel_shape=(4, 4, 4), energy_per_voxel=3.5)

    # Define a sample guiding path (sequence of 3D coordinates)
    sample_path = [(5, 5, 5), (5, 5, 6), (5, 5, 7), (6, 5, 7), (7, 5, 7)]

    tools = [point_drill, linear_cutter, explosive_charge]

    print("\n--- Running Predictive Carving Analysis ---")
    for tool in tools:
        result = predictor.evaluate_trajectory(tool, sample_path)
        print(f"Tool: {result['tool']}")
        print(f"  Feasible: {result['feasible']}")
        print(f"  Energy Cost: {result['projected_energy_cost']}")
        print(f"  Material Extracted: {result['voxels_extracted']} voxels")
        print(f"  Structural Risk: {result['structural_risk']}\n")

if __name__ == "__main__":
    main()
