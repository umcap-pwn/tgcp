import psutil
import platform
from datetime import datetime

def get_cpu_usage():
    """Получение загрузки CPU в процентах"""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Получение использования оперативной памяти"""
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    """Получение информации о дисках"""
    disks = []
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disks.append({
                'device': partition.device,
                'mountpoint': partition.mountpoint,
                'total': usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent
            })
        except Exception as e:
            print(f"Error getting disk info for {partition.mountpoint}: {e}")
    return disks

def get_system_info():
    """Получение общей информации о системе"""
    return {
        'platform': platform.system(),
        'platform_release': platform.release(),
        'platform_version': platform.version(),
        'architecture': platform.machine(),
        'processor': platform.processor(),
        'boot_time': datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    }

def get_network_info():
    """Получение информации о сетевых интерфейсах"""
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }

def format_disk_info(disks):
    """Форматирование информации о дисках для вывода"""
    result = []
    for disk in disks:
        result.append(
            f"📁 {disk['device']} ({disk['mountpoint']}):\n"
            f"  Использовано: {disk['percent']}%\n"
            f"  Свободно: {psutil._common.bytes2human(disk['free'])}\n"
            f"  Всего: {psutil._common.bytes2human(disk['total'])}"
        )
    return "\n".join(result)

def get_system_status():
    """Получение полного статуса системы"""
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disks = get_disk_usage()
    network = get_network_info()
    
    status = (
        f"🖥️ Статус системы:\n\n"
        f"💻 CPU: {cpu}%\n"
        f"🧠 RAM: {memory}%\n\n"
        f"📊 Диски:\n{format_disk_info(disks)}\n\n"
        f"🌐 Сеть:\n"
        f"  Отправлено: {psutil._common.bytes2human(network['bytes_sent'])}\n"
        f"  Получено: {psutil._common.bytes2human(network['bytes_recv'])}"
    )
    
    return status 