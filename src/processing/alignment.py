import numpy as np
import trimesh

def compute_initial_alignment(stock_mesh, target_mesh):
    """
    Computes the initial bounding box alignment and transformation matrix 
    to position the target model inside the physical stock material.
    """
    # Compute oriented bounding boxes
    stock_box = stock_mesh.bounding_box_oriented
    target_box = target_mesh.bounding_box_oriented
    
    # Calculate translation matrix to align centroids
    translation = stock_mesh.centroid - target_mesh.centroid
    target_mesh.apply_translation(translation)
    
    return target_mesh, translation

def calculate_removal_volume(stock_mesh, target_mesh):
    """
    Calculates the rough volume of material that needs to be removed.
    """
    stock_vol = stock_mesh.volume
    target_vol = target_mesh.volume
    estimated_removal = max(0.0, stock_vol - target_vol)
    
    return {
        "stock_volume": stock_vol,
        "target_volume": target_vol,
        "estimated_removal_volume": estimated_removal
    }
  
