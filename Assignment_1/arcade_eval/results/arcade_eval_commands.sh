#!/bin/bash
set -e

cd /scratch/hpc-prf-dssecs/group4/arcade_eval

echo 'A2A: ARC_QODO_VS_WCA_UEM'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_A2a.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/arc_qodo.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uem.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/ARC_QODO_VS_WCA_UEM_a2a.txt 2>&1

echo 'CVG: ARC_QODO_VS_WCA_UEM'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_Cvg.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/arc_qodo.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uem.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/ARC_QODO_VS_WCA_UEM_cvg.txt 2>&1

echo 'A2A: ARC_QODO_VS_WCA_UEMNM'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_A2a.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/arc_qodo.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uemnm.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/ARC_QODO_VS_WCA_UEMNM_a2a.txt 2>&1

echo 'CVG: ARC_QODO_VS_WCA_UEMNM'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_Cvg.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/arc_qodo.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uemnm.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/ARC_QODO_VS_WCA_UEMNM_cvg.txt 2>&1

echo 'A2A: ARC_QODO_VS_LIMBO_IL'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_A2a.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/arc_qodo.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/limbo_il.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/ARC_QODO_VS_LIMBO_IL_a2a.txt 2>&1

echo 'CVG: ARC_QODO_VS_LIMBO_IL'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_Cvg.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/arc_qodo.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/limbo_il.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/ARC_QODO_VS_LIMBO_IL_cvg.txt 2>&1

echo 'A2A: WCA_UEM_VS_WCA_UEMNM'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_A2a.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uem.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uemnm.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/WCA_UEM_VS_WCA_UEMNM_a2a.txt 2>&1

echo 'CVG: WCA_UEM_VS_WCA_UEMNM'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_Cvg.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uem.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uemnm.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/WCA_UEM_VS_WCA_UEMNM_cvg.txt 2>&1

echo 'A2A: WCA_UEM_VS_LIMBO_IL'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_A2a.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uem.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/limbo_il.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/WCA_UEM_VS_LIMBO_IL_a2a.txt 2>&1

echo 'CVG: WCA_UEM_VS_LIMBO_IL'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_Cvg.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uem.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/limbo_il.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/WCA_UEM_VS_LIMBO_IL_cvg.txt 2>&1

echo 'A2A: WCA_UEMNM_VS_LIMBO_IL'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_A2a.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uemnm.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/limbo_il.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/WCA_UEMNM_VS_LIMBO_IL_a2a.txt 2>&1

echo 'CVG: WCA_UEMNM_VS_LIMBO_IL'
java -jar /scratch/hpc-prf-dssecs/group4/arcade_eval/tools/arcade_core_Cvg.jar /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/wca_uemnm.rsf /scratch/hpc-prf-dssecs/group4/arcade_eval/rsf/limbo_il.rsf > /scratch/hpc-prf-dssecs/group4/arcade_eval/results/WCA_UEMNM_VS_LIMBO_IL_cvg.txt 2>&1

