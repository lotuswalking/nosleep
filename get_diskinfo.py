import psutil

def getDiskInformation():
    disk_info = psutil.disk_partitions(all=True)
    for disk in disk_info:
        print("Device:", disk.device)
        print("Mountpoint:", disk.mountpoint)
        print("File system type:", disk.fstype)
        print("Options:", disk.opts)
        print("")


def main():
    getDiskInformation()

if __name__ == "__main__":
    main()
