import torch
from collections import OrderedDict
import argparse

def load_checkpoint(checkpoint_path):
    """
    Load a PyTorch checkpoint file and return its state dict with essential analytics
    """
    try:
        state_dict = torch.load(checkpoint_path, map_location='cpu')
        
        # Extract model state based on checkpoint structure
        if isinstance(state_dict, OrderedDict):
            model_state = state_dict
        elif isinstance(state_dict, dict):
            if 'state_dict' in state_dict:
                model_state = state_dict['state_dict']
            elif 'model_state_dict' in state_dict:
                model_state = state_dict['model_state_dict']
            elif 'model' in state_dict:
                model_state = state_dict['model']
            else:
                model_state = state_dict
        
        print(f"\nCheckpoint loaded from: {checkpoint_path}")
        print(f"Type of loaded state: {type(model_state)}")
        
        # Calculate model statistics
        total_params = 0
        total_bytes = 0
        layer_types = {}
        
        print("\nModel Analysis:")
        print("-" * 50)
        
        # Access model weights from the nested structure
        model_weights = model_state['state']['model']
        
        for name, param in model_weights.items():
            if isinstance(param, torch.Tensor):
                # Parameter count and memory
                num_params = param.numel()
                total_params += num_params
                bytes_used = param.element_size() * num_params
                total_bytes += bytes_used
                
                # Layer type analysis
                parts = name.split('.')
                if 'bert' in parts:
                    layer_type = parts[parts.index('bert') + 1]
                else:
                    layer_type = parts[0]
                
                layer_types[layer_type] = layer_types.get(layer_type, 0) + num_params
                
                # Print layer statistics
                if param.dtype in [torch.float32, torch.float16]:
                    print(f"\n{name}:")
                    print(f"  Shape: {param.shape}")
                    print(f"  Parameters: {num_params:,}")
                    print(f"  Memory: {bytes_used/1024/1024:.2f} MB")
                    print(f"  Stats: min={param.min().item():.4f}, max={param.max().item():.4f}, "
                          f"mean={param.mean().item():.4f}, std={param.std().item():.4f}")
        
        # Print summary
        print("\nSummary:")
        print(f"Total Parameters: {total_params:,}")
        print(f"Total Model Size: {total_bytes/1024/1024:.2f} MB")
        
        print("\nParameter Distribution by Layer Type:")
        for layer_type, count in sorted(layer_types.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_params) * 100
            print(f"{layer_type}: {count:,} parameters ({percentage:.1f}%)")
        
        return model_state
    
    except Exception as e:
        print(f"Error loading checkpoint: {str(e)}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--checkpoint_path', '-c', type=str, required=True, help="Path to model checkpoint")
    args = parser.parse_args()
    state_dict = load_checkpoint(args.checkpoint_path)
