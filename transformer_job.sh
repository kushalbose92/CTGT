#!/bin/bash
#SBATCH --job-name=myjob             # name shown in the queue
#SBATCH --time=02:00:00              # max run time (HH:MM:SS)
#SBATCH --nodes=1                    # number of nodes
#SBATCH --ntasks=1                   # number of processes
#SBATCH --cpus-per-task=4            # CPU cores per process
#SBATCH --mem=16G                    # memory for the job
#SBATCH --gpus=1                     # number of GPUs (remove this line for a CPU-only job)
#SBATCH --output=myjob_%j.out        # standard output (%j = job ID)
#SBATCH --error=myjob_%j.err         # error messages
 
# Go to your work directory (Triton's main storage for code and data)
cd /scratch/work/$USER/myproject
 
# Load Python and activate your conda environment
module load mamba
source activate /scratch/work/$USER/conda/myenv
 
# Show which node and GPU the job got (useful for debugging)
echo "Running on node: $(hostname)"
nvidia-smi
 
# Run your code
sh run_superpixels.sh