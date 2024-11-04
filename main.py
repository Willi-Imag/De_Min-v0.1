""" Python3 docu-docu """
"""
"""
import psutil, GPUtil
"""@~@"""
cpu_temp = psutil.sensors_temperatures()['k10temp'][0].current
gpu = GPUtil.getGPUs()[0]
gpu_temp = gpu.temperature
"""@~@"""
print (f"CPU temp: {cpu_temp}")
print (f"GPU temp: {gpu_temp}")
