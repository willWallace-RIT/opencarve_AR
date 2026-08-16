# opencarve_AR
AR carving guidance using raw material assessment and stl file

# AR Subtractive Carving

A framework for manual subtractive carving guided by augmented reality. This system assesses raw stock material against a target 3D STL model and projects real-time carving guides (contour maps, depth heatmaps) to assist manual material removal without CNC machinery.

## Architecture
- **Acquisition:** Captures the current physical state of the stock using RGB-D camera tech.
- **Processing:** Aligns target STL with stock, computes material removal volumes, and generates iterative carving layers.
- **Vision:** Tracks physical block state and manages real-time calibration for projector-based AR.
- **UI:** Projects visual overlays onto the workpiece to indicate material to be removed.

## Getting Started
1. Configure `configs/default_pipeline.yaml` with your camera/projector intrinsics.
2. Place raw stock scans in `data/raw_stock_scans/`.
3. Place target 3D models in `data/target_stls/`.
4. Run `scripts/run_pipeline.py` to initiate the projection alignment.
5. 
